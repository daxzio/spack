# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RiscvOpenocd(AutotoolsPackage):
    """The Open On-Chip Debugger (OpenOCD) aims to provide debugging, in-system
    programming and boundary-scan testing for embedded target devices.
    """

    homepage = "https://openocd.org/"
    url = "https://github.com/riscv-collab/riscv-openocd/archive/refs/tags/v2018.12.0.tar.gz"
    git = "https://github.com/riscv-collab/riscv-openocd.git"

    maintainers("davekeeshan")

    license("GPL-2.0-or-later")

    version("master", branch="master")

    version("2025.01.07", commit="c4ea6d18d003435c90c150e8acb511019591f2e8", submodules=True)
    version("2024.11.21", commit="1bf7efb2d5be792116bad3d0d7cfb812228d18ea", submodules=True)
    version("2018.12.0", commit="c3c76bfafa6612dc56b3914c9f93eb2a790ef87b", submodules=True)

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    variant("remotebitbang", default=False, description="build with remote bitbang support")
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

        if spec.satisfies("+remotebitbang"):
            args.append("--enable-remote-bitbang")
        args.extend(self.enable_or_disable("ftdi"))
        args.extend(self.enable_or_disable("linuxgpiod"))
        args.extend(self.enable_or_disable("bcm2835gpio"))

        return args

    def setup_run_environment(self, env):
        env.prepend_path("OPENOCD_SCRIPTS", f"{self.prefix}/share/openocd/scripts")
