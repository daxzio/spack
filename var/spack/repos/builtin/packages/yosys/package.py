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

    version("0.5",  sha256="f2adb8115f95e9613838fc545bad94dcfe7c8afcfb092595c1b6996f81eadfac")
    version("0.20", sha256="ee261487badf1b554616d555da8496a7c84ef21ae66a979ddd946b6949a780a4")
    version("0.34", sha256="57897bc3fe5fdc940e9f3f3ae03b84f5f8e9149b6f26d3699f7ecb9f31a41ae0")

    depends_on("automake")
    depends_on("readline")
    depends_on("pkg-config")
    depends_on("tcl")
    depends_on("llvm")
    #depends_on("gcc@8.4:", type=("build", "run"))
    #depends_on("gcc@8.4:")

    def edit(self, spec, prefix):
        env['PREFIX'] = prefix
        env['LDFLAGS'] = f"-I${spec['ncurses'].prefix.lib}"
        env['CFLAGS'] = f"-I${spec['ncurses'].prefix.include}"
        #env['ENABLE_READLINE'] = 0

#      def build(self, spec, prefix):
#          options = [
#              'SHLIB_LIBS=-L{0} -lncursesw'.format(spec['ncurses'].prefix.lib)
#          ]
#          make(*options)
