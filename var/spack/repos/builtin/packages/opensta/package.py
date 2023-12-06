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

    # version("1.1.0", sha256="f0be81afe643adc2452055e5485f09cdb509a8fdd5a4ec5547b0c31dd22b4830")
    variant("cudd", default=True, description="build with cudd support")

    depends_on("flex", type="build")
    depends_on("tcl@8.6.11", type="build")
    depends_on("swig", type="build")
    depends_on("zlib", type="build")
    depends_on("llvm")
    depends_on("cudd", type="build", when="+cudd")

    def cmake_args(self):
        args = []
        # args.append(f"-DCMAKE_CXX_FLAGS=-I{self.spec['zlib'].prefix.include}")
        args.append(f"-DZLIB_ROOT=-{self.spec['zlib'].prefix}")
        if self.spec.satisfies("+cudd"):
            args.append("-DUSE_CUDD=ON ")
            args.append(f"-DCUDD_DIR={self.spec['cudd'].prefix}")

        return args
