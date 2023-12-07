# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Opensta(CMakePackage):
    """
    OpenSTA is a gate level static timing verifier. As a stand-alone executable
    it can be used to verify the timing of a design using standard file formats.

    * Verilog netlist
    * Liberty library
    * SDC timing constraints
    * SDF delay annotation
    * SPEF parasitics

    """

    homepage = "https://github.com/parallaxsw/OpenSTA"
    git = "https://github.com/parallaxsw/OpenSTA.git"
    # git = "https://github.com/The-OpenROAD-Project/OpenSTA.git"

    maintainers("davekeeshan")

    version("master", branch="master")

    variant("zlib", default=True, description="build with zlib support")
    variant("cudd", default=True, description="build with cudd support")

    depends_on("flex", type="build")
    depends_on("tcl@8.6.11", type="build")
    depends_on("swig", type="build")
    depends_on("zlib", type="build", when="+zlib")
    depends_on("llvm", type="build")
    depends_on("cudd", type="build", when="+cudd")

    def cmake_args(self):
        args = []
        if self.spec.satisfies("+zlib"):
            # args.append(f"-DCMAKE_CXX_FLAGS=-I{self.spec['zlib'].prefix.include}")
            args.append(f"-DZLIB_ROOT={self.spec['zlib'].prefix}")
        if self.spec.satisfies("+cudd"):
            args.append("-DUSE_CUDD=ON ")
            args.append(f"-DCUDD_DIR={self.spec['cudd'].prefix}")

        return args
