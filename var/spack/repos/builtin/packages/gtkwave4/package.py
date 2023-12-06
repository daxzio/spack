# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Gtkwave4(MesonPackage):
    """GTKWave is a fully featured GTK+ based wave viewer for Unix, Win32, and
    Mac OSX which reads LXT, LXT2, VZT, FST, and GHW files as well as standard
    Verilog VCD/EVCD files and allows their viewing.
    """

    homepage = "https://gtkwave.sourceforge.net/"
    git = "https://github.com/gtkwave/gtkwave.git"

    maintainers("davekeeshan")

    version("master", branch="master")

    depends_on("meson", type="build")
    depends_on("ninja", type="build")
    depends_on("glib", type="build")
    depends_on("cmake", type="build")
    depends_on("gperf", type="build")
    depends_on("flex", type="build")
    depends_on("gtkplus", type="build")
    depends_on("judy", type="build")
    depends_on("zlib", type="build")
    depends_on("bzip2", type="build")
    depends_on("tcl", type="build")
    depends_on("tk", type="build")
    depends_on("desktop-file-utils", type="build")
    depends_on("gobject-introspection", type="build")

    def configure_args(self):
        args = [
            f"--prefix={self.prefix}",
            "-Dc_link_args='-ldl'",
            f"-Dc_args='-I{self.spec['zlib'].prefix.include} -I{self.spec['bzip2'].prefix.include}'",
        ]
        return args
