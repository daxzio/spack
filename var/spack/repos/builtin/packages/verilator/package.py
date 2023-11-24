# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Verilator(AutotoolsPackage):
    """Verilator is the fastest free Verilog HDL simulator.

    It compiles synthesizable Verilog (not test-bench code!), plus some PSL,
    SystemVerilog and Synthesis assertions into C++ or SystemC code. It is
    designed for large projects where fast simulation performance is of primary
    concern, and is especially well suited to generate executable models of
    CPUs for embedded software design teams.

    Please do not download this program if you are expecting a full featured
    replacement for NC-Verilog, VCS or another commercial Verilog simulator
    or Verilog compiler for a little project! (Try Icarus instead.) However, if
    you are looking for a path to migrate synthesizable Verilog to C++ or
    SystemC, and writing just a touch of C code and Makefiles doesn't scare you
    off, this is the free Verilog compiler for you.

    Verilator supports the synthesis subset of Verilog, plus initial
    statements, proper blocking/non-blocking assignments, functions, tasks,
    multi-dimensional arrays, and signed numbers. It also supports very simple
    forms of SystemVerilog assertions and coverage analysis. Verilator supports
    the more important Verilog 2005 constructs, and some SystemVerilog
    features, with additional constructs being added as users request them.

    Verilator has been used to simulate many very large multi-million gate
    designs with thousands of modules."""

    homepage = "https://www.veripool.org/projects/verilator"
    url = "https://github.com/verilator/verilator/archive/refs/tags/v5.018.tar.gz"
    git = "https://github.com/verilator/verilator.git"

    version("5.018", sha256="8b544273eedee379e3c1a3bb849e14c754c9b5035d61ad03acdf3963092ba6c0")
    version("5.016", sha256="66fc36f65033e5ec904481dd3d0df56500e90c0bfca23b2ae21b4a8d39e05ef1")
    version("5.014", sha256="36e16c8a7c4b376f88d87411cea6ee68710e6d1382a13faf21f35d65b54df4a7")
    version("4.108", sha256="ce521dc57754e5a325ff7000c434ce23674c8e1de30e1f2a6506dc3a33bd7c55")
    
#     version("4.020", sha256="e19ccbaad305d7aa2a0e56fc1a1629c4db1b4abd7f4530b9c035ee715217f3f2")
#     version("3.920", sha256="2b5c38aa432d0766a38475219f9548d64d18104ce8bdcb5d29e42f5da06943ff")
#     version("3.904", sha256="ea95e08b2d70682ad42e6c2f5ba99f59b2e7b220791214076099cdf6b7a8c1cb")

    maintainers("davekeeshan")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("help2man", type="build")
    depends_on("bison", type="build")
    depends_on("flex", type="build")
    depends_on("ccache", type=("build", "run"))
    depends_on("perl", type=("build", "run"))
    depends_on("bash", type="build")

    def setup_run_environment(self, env):
        env.prepend_path("VERILATOR_ROOT", self.prefix)

    def autoreconf(self, spec, prefix):
        which("bash")("autoconf")

    # verilator requires access to its shipped scripts (bin) and include
    # but the standard make doesn't put it in the correct places
    @run_before("install")
    def install_include(self):
        install_tree("include", prefix.include)
        install_tree("bin", prefix.bin)

    # we need to fix the CXX and LINK paths, as they point to the spack
    # wrapper scripts which aren't usable without spack
    @run_after("install")
    def patch_cxx(self):
        filter_file(
            r"^CXX\s*=.*",
            f"CXX = {self.compiler.cxx}",
            join_path(self.prefix.include, "verilated.mk"),
        )
        filter_file(
            r"^LINK\s*=.*",
            f"LINK = {self.compiler.cxx}",
            join_path(self.prefix.include, "verilated.mk"),
        )
