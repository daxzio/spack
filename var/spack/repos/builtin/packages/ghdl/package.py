# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Ghdl(AutotoolsPackage):
    """GHDL is a shorthand for G Hardware Design Language (currently, G has no 
    meaning). It is a VHDL analyzer, compiler, simulator and (experimental) 
    synthesizer that can process (nearly) any VHDL design."""

    homepage = "https://ghdl.github.io/ghdl"
    git = "https://github.com/ghdl/ghdl.git"

    version(
        "3.0.0", 
        sha256="c1ed4d2095df80131260a48c55bb53409ce8d4c38bba42618ca040115faf08b9", 
        url = "https://github.com/ghdl/ghdl/archive/refs/tags/v3.0.0.tar.gz"
    )

    maintainers("davekeeshan")
    
    variant("llvm", default=False, description="build with llvm support")

    depends_on("llvm@14", when="+llvm")
    
    #conflicts("%gcc@12:", when="+llvm")

    def configure_args(self):
        args = []
        if self.spec.satisfies("+llvm"):
            args.append("--with-llvm-config")
        
        return args
