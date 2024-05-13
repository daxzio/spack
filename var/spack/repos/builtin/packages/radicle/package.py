# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Radicle(Package):
    """Radicle Heartwood Protocol & Stack

    Heartwood is the third iteration of the Radicle Protocol, a powerful 
    peer-to-peer code collaboration and publishing stack. The repository contains 
    a full implemention of Heartwood, complete with a user-friendly command-line 
    interface (rad) and network daemon (radicle-node).

    Radicle was designed to be a secure, decentralized and powerful alternative 
    to code forges such as GitHub and GitLab that preserves user sovereignty 
    and freedom.
    """

    homepage = "https://radicle.xyz/"
    git = "https://seed.radicle.xyz/z3gqcJUoA1n9HaHKufZs5FCSGazv5.git"

    maintainers("davekeeshan")

    license("MIT")

    version("master", branch="master")
#     version("0.8.0", commit="f15afa84be7bda050bfb93e321bbce28b56d10b6")
    version("1.0.0-rc.8", commit="0d880e12")
    version("1.0.0-rc.7", commit="9cd08a01")
    version("1.0.0-rc.6", commit="7126d051")
    version("1.0.0-rc.5", commit="c6076196")
    version("1.0.0-rc.4", commit="35567583")
    version("1.0.0-rc.3", commit="bd8e0ebc")
    version("1.0.0-rc.2", commit="ea69168f")
    version("0.8.0", commit="f15afa8")

    depends_on("git", type="run")
    depends_on("openssh", type="run")
    depends_on("rust", type="build")
    depends_on("rust@1.77:", when="@1.0.0-rc.2", type="build")

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("install", "--root", prefix, "--path", "radicle-cli",  "--force", "--locked")
        cargo("install", "--root", prefix, "--path", "radicle-node",  "--force", "--locked")
        cargo("install", "--root", prefix, "--path", "radicle-remote-helper",  "--force", "--locked")
