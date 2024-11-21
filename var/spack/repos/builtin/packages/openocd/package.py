# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Openocd(AutotoolsPackage):
    """The Open On-Chip Debugger (OpenOCD) aims to provide debugging, in-system
    programming and boundary-scan testing for embedded target devices.
    """

    homepage = "https://openocd.org/"
    url = "https://github.com/openocd-org/openocd/archive/refs/tags/v0.12.0.tar.gz"
    git = "https://github.com/openocd-org/openocd.git"

    maintainers("davekeeshan")

    license("GPL-2.0-or-later")

    version("master", branch="master")

    version("0.12.0", commit="9ea7f3d647c8ecf6b0f1424002dfc3f4504a162c", submodules=True)

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    variant("remote-bitbang", default=False, description="build with remote bitbang support")
    variant("ftdi", default=False, description="build with ftdi support")
    variant("linuxgpiod", default=False, description="build with linux gpio support")
    variant("bcm2835gpio", default=False, description="build with bcm2835gpio support")

    depends_on("automake", type="build")
    depends_on("autoconf", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("libtool", type="build")
    depends_on("libusb", type="build", when="+ftdi")
    depends_on("libftdi", type="build", when="+ftdi")
    depends_on("libgpiod@:1.6", type="build", when="+linuxgpiod")

    def autoreconf(self, spec, prefix):
        bash = which("bash")
        bash("./bootstrap")

    def configure_args(self):
        spec = self.spec
        args = []

        args.extend(self.enable_or_disable("remote-bitbang"))
        args.extend(self.enable_or_disable("ftdi"))
        args.extend(self.enable_or_disable("linuxgpiod"))
        args.extend(self.enable_or_disable("bcm2835gpio"))

        return args
