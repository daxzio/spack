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

    #version("0.20", sha256="9764380f6e187cb4344334e1e921ec3206ff6ae3105e3a8d5e56ac49301c433b")
    version("0.34", sha256="57897bc3fe5fdc940e9f3f3ae03b84f5f8e9149b6f26d3699f7ecb9f31a41ae0")

    depends_on("automake")
    #depends_on("readline")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        src = "./"
#         binaries = ['abc', 'arch_flags']
        binaries = [
            'yosys', 
            'yosys-config',             '', 
            'yosys-abc', 
            'yosys-filterlib', 
            'yosys-smtbmc', 
            'yosys-witness', 
#             '', 
            ]
        for b in binaries:
            install(join_path(src, b), join_path(prefix.bin, b))

