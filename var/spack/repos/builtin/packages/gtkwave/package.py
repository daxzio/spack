# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Gtkwave(AutotoolsPackage):
    """GTKWave is a fully featured GTK+ based wave viewer for Unix, Win32, and 
    Mac OSX which reads LXT, LXT2, VZT, FST, and GHW files as well as standard 
    Verilog VCD/EVCD files and allows their viewing.
    """

    homepage = "https://gtkwave.sourceforge.net/"
    #url = "https://sourceforge.net/projects/gtkwave/files/gtkwave-gtk3-3.3.117/gtkwave-gtk3-3.3.117.tar.gz"
    git = "https://github.com/gtkwave/gtkwave.git"
    url = "https://github.com/gtkwave/gtkwave/archive/refs/tags/v3.3.116.tar.gz"

    maintainers("davekeeshan")

    version("3.3.116", sha256="b178398da32f8e1958db74057fec278fe0fcc3400485f20ded3ab2330c58f598")
    version("3.3.115", sha256="93871161d64d11b7f1dc9e88e0498e9f83198c0cb04eb4b5099348c98981c347")
    version("3.3.111", sha256="22f4be02825cf4b3490c7a9c809abb3dbf0019e6a168d1c2239c66b2c8250741")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("tcl", type="build")
    depends_on("tk", type="build")

    configure_directory = build_directory = "gtkwave3-gtk3"

    def configure_args(self):
        args = []
    
        args.append(f"--with-tcl={self.spec['tcl'].prefix.lib}")
        args.append(f"--with-tk={self.spec['tk'].prefix.lib}")
        args.append("--enable-gtk3")
        args.append("--disable-mime-update")

        return args
