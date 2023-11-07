# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Xnedit(MakefilePackage):
    """XNEdit is a multi-purpose text editor for the X Window System, which 
    combines a standard, easy to use, graphical user interface with the thorough 
    functionality and stability required by users who edit text eight hours a 
    day. It provides intensive support for development in a wide variety of 
    languages, text processors, and other tools, but at the same time can be 
    used productively by just about anyone who needs to edit text.

    XNEdit is a fork of the Nirvana Editor (NEdit) and provides new 
    functionality like antialiased text rendering and support for unicode.
    """

    homepage = "https://www.unixwork.de/xnedit/"
    url = "https://github.com/unixwork/xnedit/archive/refs/tags/v1.5.2.tar.gz"
    git = "https://github.com/unixwork/xnedit.git"

    version("1.5.2", sha256="2f9710b661f8ec5d371a3385fa480c7424e2f863938a8e2ae71cb17397be3f91")

    depends_on("automake")
    #depends_on("libx11", when="+x")
    depends_on("libx11")
#     depends_on("libxpm")
#     depends_on("libiconv", type=("build", "run"))

    def build(self, spec, prefix):
        make("linux")

    def install(self, spec, prefix):
        make("install", f"PREFIX={prefix}")
