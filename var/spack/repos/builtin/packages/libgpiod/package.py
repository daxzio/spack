# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Libgpiod(AutotoolsPackage):
    """C library and tools for interacting with the linux GPIO character device (gpiod stands for GPIO device)"""

    homepage = "https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/about/"
    url = "https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-2.2.tar.gz"
    git = "https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod"

    maintainers("davekeeshan")

    license("LGPL-2.1-or-later")

    version("master", branch="master")
    version("2.2", sha256="ae35329db7027c740e90c883baf27c26311f0614e6a7b115771b28188b992aec")
    version("2.1.3", sha256="8d80ea022ae78122aa525308e7423b83064bff278fcd9cd045b94b4f81f8057d")
    version("2.0", sha256="62071ac22872d9b936408e4a067d15edcdd61dce864ace8725eacdaefe23b898")
    version("1.6.4", sha256="829d4ac268df07853609d67cfc7f476e9aa736cb2a68a630be99e8fad197be0a")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("autoconf-archive", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    def autoreconf(self, spec, prefix):
        bash = which("bash")
        bash("./autogen.sh")
