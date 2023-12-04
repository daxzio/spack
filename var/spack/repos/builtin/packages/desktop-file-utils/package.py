# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class DesktopFileUtils(MesonPackage):
    """The GTK+ package contains libraries used for creating graphical user
    interfaces for applications."""

    homepage = "https://www.freedesktop.org/software/desktop-file-utils"
    url = "https://www.freedesktop.org/software/desktop-file-utils/releases/desktop-file-utils-0.27.tar.xz"

    version("0.27", sha256="a0817df39ce385b6621880407c56f1f298168c040c2032cedf88d5b76affe836")

    # See meson.build for version requirements
    depends_on("meson", type="build")
    depends_on("ninja", type="build")
    depends_on("glib", type="build")
    depends_on("cmake", type="build")
