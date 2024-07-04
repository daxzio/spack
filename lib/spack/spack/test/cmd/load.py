# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os
import re
import sys

import pytest

import spack.spec
import spack.user_environment as uenv
import spack.util.environment
from spack.main import SpackCommand

load = SpackCommand("load")
unload = SpackCommand("unload")
install = SpackCommand("install")
location = SpackCommand("location")


def test_manpath_trailing_colon(
    install_mockery, mock_fetch, mock_archive, mock_packages, working_env
):
    (shell, set_command, commandsep) = (
        ("--bat", 'set "%s=%s"', "\n")
        if sys.platform == "win32"
        else ("--sh", "export %s=%s", ";")
    )

    """Test that the commands generated by load add the MANPATH prefix
    inspections. Also test that Spack correctly preserves the default/existing
    manpath search path via a trailing colon"""
    install("mpileaks")

    sh_out = load(shell, "mpileaks")
    lines = [line.strip("\n") for line in sh_out.split(commandsep)]
    assert any(re.match(set_command % ("MANPATH", ".*" + os.pathsep), ln) for ln in lines)
    os.environ["MANPATH"] = "/tmp/man" + os.pathsep

    sh_out = load(shell, "mpileaks")
    lines = [line.strip("\n") for line in sh_out.split(commandsep)]
    assert any(
        re.match(set_command % ("MANPATH", ".*" + os.pathsep + "/tmp/man" + os.pathsep), ln)
        for ln in lines
    )


def test_load_recursive(install_mockery, mock_fetch, mock_archive, mock_packages, working_env):
    def test_load_shell(shell, set_command):
        """Test that `spack load` applies prefix inspections of its required runtime deps in
        topo-order"""
        install("mpileaks")
        mpileaks_spec = spack.spec.Spec("mpileaks").concretized()

        # Ensure our reference variable is clean.
        os.environ["CMAKE_PREFIX_PATH"] = "/hello" + os.pathsep + "/world"

        shell_out = load(shell, "mpileaks")

        def extract_value(output, variable):
            match = re.search(set_command % variable, output, flags=re.MULTILINE)
            value = match.group(1)
            return value.split(os.pathsep)

        # Map a prefix found in CMAKE_PREFIX_PATH back to a package name in mpileaks' DAG.
        prefix_to_pkg = lambda prefix: next(
            s.name for s in mpileaks_spec.traverse() if s.prefix == prefix
        )

        paths_shell = extract_value(shell_out, "CMAKE_PREFIX_PATH")

        # We should've prepended new paths, and keep old ones.
        assert paths_shell[-2:] == ["/hello", "/world"]

        # All but the last two paths are added by spack load; lookup what packages they're from.
        pkgs = [prefix_to_pkg(p) for p in paths_shell[:-2]]

        # Do we have all the runtime packages?
        assert set(pkgs) == set(
            s.name for s in mpileaks_spec.traverse(deptype=("link", "run"), root=True)
        )

        # Finally, do we list them in topo order?
        for i, pkg in enumerate(pkgs):
            set(s.name for s in mpileaks_spec[pkg].traverse(direction="parents")) in set(pkgs[:i])

        # Lastly, do we keep track that mpileaks was loaded?
        assert (
            extract_value(shell_out, uenv.spack_loaded_hashes_var)[0] == mpileaks_spec.dag_hash()
        )
        return paths_shell

    if sys.platform == "win32":
        shell, set_command = ("--bat", r'set "%s=(.*)"')
        test_load_shell(shell, set_command)
    else:
        params = [("--sh", r"export %s=([^;]*)"), ("--csh", r"setenv %s ([^;]*)")]
        shell, set_command = params[0]
        paths_sh = test_load_shell(shell, set_command)
        shell, set_command = params[1]
        paths_csh = test_load_shell(shell, set_command)
        assert paths_sh == paths_csh


@pytest.mark.parametrize(
    "shell,set_command",
    (
        [("--bat", 'set "%s=%s"')]
        if sys.platform == "win32"
        else [("--sh", "export %s=%s"), ("--csh", "setenv %s %s")]
    ),
)
def test_load_includes_run_env(
    shell, set_command, install_mockery, mock_fetch, mock_archive, mock_packages
):
    """Tests that environment changes from the package's
    `setup_run_environment` method are added to the user environment in
    addition to the prefix inspections"""
    install("mpileaks")

    shell_out = load(shell, "mpileaks")

    assert set_command % ("FOOBAR", "mpileaks") in shell_out


def test_load_first(install_mockery, mock_fetch, mock_archive, mock_packages):
    """Test with and without the --first option"""
    shell = "--bat" if sys.platform == "win32" else "--sh"
    install("libelf@0.8.12")
    install("libelf@0.8.13")

    # Now there are two versions of libelf, which should cause an error
    out = load(shell, "libelf", fail_on_error=False)
    assert "matches multiple packages" in out
    assert "Use a more specific spec" in out

    # Using --first should avoid the error condition
    load(shell, "--first", "libelf")


def test_load_fails_no_shell(install_mockery, mock_fetch, mock_archive, mock_packages):
    """Test that spack load prints an error message without a shell."""
    install("mpileaks")

    out = load("mpileaks", fail_on_error=False)
    assert "To set up shell support" in out


@pytest.mark.parametrize(
    "shell,set_command,unset_command",
    (
        [("--bat", 'set "%s=%s"', 'set "%s="')]
        if sys.platform == "win32"
        else [("--sh", "export %s=%s", "unset %s"), ("--csh", "setenv %s %s", "unsetenv %s")]
    ),
)
def test_unload(
    shell,
    set_command,
    unset_command,
    install_mockery,
    mock_fetch,
    mock_archive,
    mock_packages,
    working_env,
):
    """Tests that any variables set in the user environment are undone by the
    unload command"""
    install("mpileaks")
    mpileaks_spec = spack.spec.Spec("mpileaks").concretized()

    # Set so unload has something to do
    os.environ["FOOBAR"] = "mpileaks"
    os.environ[uenv.spack_loaded_hashes_var] = ("%s" + os.pathsep + "%s") % (
        mpileaks_spec.dag_hash(),
        "garbage",
    )

    shell_out = unload(shell, "mpileaks")

    assert (unset_command % "FOOBAR") in shell_out

    assert set_command % (uenv.spack_loaded_hashes_var, "garbage") in shell_out


def test_unload_fails_no_shell(
    install_mockery, mock_fetch, mock_archive, mock_packages, working_env
):
    """Test that spack unload prints an error message without a shell."""
    install("mpileaks")
    mpileaks_spec = spack.spec.Spec("mpileaks").concretized()
    os.environ[uenv.spack_loaded_hashes_var] = mpileaks_spec.dag_hash()

    out = unload("mpileaks", fail_on_error=False)
    assert "To set up shell support" in out
