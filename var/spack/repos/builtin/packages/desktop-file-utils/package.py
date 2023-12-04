# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class DesktopFileUtils(MesonPackage):
    """desktop-file-utils contains a few command line utilities for working with desktop entries:

        * desktop-file-validate: validates a desktop file and prints warnings/errors about desktop 
          entry specification violations.
        * desktop-file-install: installs a desktop file to the applications directory, optionally 
          munging it a bit in transit.
        * update-desktop-database: updates the database containing a cache of MIME types handled 
          by desktop files. It requires GLib to compile, because the implementation requires 
          Unicode utilities and such."""

    homepage = "https://www.freedesktop.org/software/desktop-file-utils"
    url = "https://www.freedesktop.org/software/desktop-file-utils/releases/desktop-file-utils-0.27.tar.xz"

    version("0.27", sha256="a0817df39ce385b6621880407c56f1f298168c040c2032cedf88d5b76affe836")

    depends_on("meson", type="build")
    depends_on("ninja", type="build")
    depends_on("glib", type="build")
    depends_on("cmake", type="build")
