# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Libftdi(MakefilePackage):
    """libftdi - A library (using libusb) to talk to FTDI's UART/FIFO chips 
    including the popular bitbang mode"""

    homepage = "https://www.intra2net.com/en/developer/libftdi/index.php"
    git = "git://developer.intra2net.com/libftdi"

    maintainers("davekeeshan")

    license("GPL-2.0-or-later")

    version("master", branch="master")
    version("1.5", commit="5c2c58e03ea999534e8cb64906c8ae8b15536c30")
    version("1.4", commit="d5c1622a2ff0c722c0dc59533748489b45774e55")
    version("1.3", commit="96d337a16b723d792f6ab5f40b7aa43120ac4782")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake", type="build")
    depends_on("libconfuse", type="build")
    depends_on("libusb", type="build")

    def build(self, spec, prefix):

        mkdirp("./build")
        os.chdir("./build")

        cmake = which("cmake")
        cmake(
            f"-DCMAKE_INSTALL_PREFIX={prefix}",
            "../",
        )

    def install(self, spec, prefix):
        make()
        make("install")

