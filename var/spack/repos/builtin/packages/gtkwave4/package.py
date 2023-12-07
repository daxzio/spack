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

    depends_on("meson")
    depends_on("ninja")
    depends_on("glib")
    depends_on("cmake")
    depends_on("gperf")
    depends_on("flex")
    depends_on("gtkplus")
    depends_on("judy")
    depends_on("zlib")
    depends_on("bzip2")
    depends_on("tcl")
    depends_on("tk")
    depends_on("desktop-file-utils")
    depends_on("gobject-introspection")

    def meson_args(self):
        args = std_meson_args
        args.extend([
#             f"--prefix={self.prefix}",
            "-Dc_link_args=-ldl",
            f"-Dc_args=-I{self.spec['zlib'].prefix.include} -I{self.spec['bzip2'].prefix.include}",
        ])
        return args
