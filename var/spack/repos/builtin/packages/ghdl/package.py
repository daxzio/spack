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
    license("GPL-2.0-or-later")

    maintainers("davekeeshan")
    
    version("master", branch="master")
    
    version(
        "4.1.0", 
        sha256="0aab531b45a6613b0918f3ac6ec717b8acfad051d1abb1c39eb7490590c7a324", 
        url = "https://github.com/ghdl/ghdl/archive/refs/tags/v4.1.0.tar.gz"
    )
    version(
        "3.0.0", 
        sha256="c1ed4d2095df80131260a48c55bb53409ce8d4c38bba42618ca040115faf08b9", 
        url = "https://github.com/ghdl/ghdl/archive/refs/tags/v3.0.0.tar.gz"
    )

    version(
        "2025.01.04", 
        sha256="f03bb9259551d067b468dba3519d3e9cb33ef680b0eeecdc775a8216aacab481", 
        url = "https://github.com/ghdl/ghdl/archive/refs/tags/nightly.tar.gz"
    )
    
    variant("llvm", default=False, description="build with llvm support")

#     depends_on("llvm@14", when="+llvm")
    depends_on("llvm@18", when="+llvm")
    depends_on("gnat-fsf")
    
    #conflicts("%gcc@12:", when="+llvm")

    def configure_args(self):
        args = []
        if self.spec.satisfies("+llvm"):
            args.append("--with-llvm-config")
        
        return args
