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

    homepage = "https://modules.readthedocs.io"
    url = "https://github.com/YosysHQ/yosys/releases/download/yosys-0.34/abc.tar.gz"

    version("0.34", sha256="b0f09893f9b1a5c2eb0c5597283b0374bbc7606bb120d23fcf558b432a216ec5")

    depends_on("automake")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        src = "./"
        binaries = ['abc', 'arch_flags']
        for b in binaries:
            install(join_path(src, b), join_path(prefix.bin, b))

