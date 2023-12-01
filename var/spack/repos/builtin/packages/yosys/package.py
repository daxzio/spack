# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Yosys(MakefilePackage):
    """Yosys is a framework for RTL synthesis tools. It currently has extensive 
    Verilog-2005 support and provides a basic set of synthesis algorithms for 
    various application domains.

    Yosys can be adapted to perform any synthesis job by combining the existing 
    passes (algorithms) using synthesis scripts and adding additional passes 
    as needed by extending the yosys C++ code base.

    Yosys is free software licensed under the ISC license (a GPL compatible 
    license that is similar in terms to the MIT license or the 2-clause BSD license).
    """

    homepage = "https://yosyshq.net/yosys"
    url = "https://github.com/YosysHQ/yosys/archive/refs/tags/yosys-0.34.tar.gz"
    git = "https://github.com/YosysHQ/yosys.git"

    version("0.34", sha256="57897bc3fe5fdc940e9f3f3ae03b84f5f8e9149b6f26d3699f7ecb9f31a41ae0")
    version("0.20", sha256="ee261487badf1b554616d555da8496a7c84ef21ae66a979ddd946b6949a780a4")
#     version("0.5",  sha256="f2adb8115f95e9613838fc545bad94dcfe7c8afcfb092595c1b6996f81eadfac")

    depends_on("automake", type="build")
    depends_on("readline")
    depends_on("pkg-config")
    depends_on("tcl")
    depends_on("zlib")
    depends_on("llvm")

    def setup_build_environment(self, env):
        env.set("PREFIX", self.prefix)
        env.set("CXXFLAGS", "-I{0}".format(self.spec['readline'].prefix.include))
        env.set("LDFLAGS", "-L{0} -L{1}".format(self.spec['readline'].prefix.lib, self.spec['zlib'].prefix.lib))
        env.set("ENABLE_ABC", "0")

#     def edit(self, spec, prefix):
#         env['PREFIX'] = prefix
#         env['LDFLAGS']  = f"-L{spec['readline'].prefix.lib} -L{spec['zlib'].prefix.lib}"
#         #env['CFLAGS']   = f"-I{spec['readline'].prefix.include}"
#         env['CXXFLAGS'] = f"-I{spec['readline'].prefix.include}"

