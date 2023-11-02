# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Verible(Package):
    """The Environment Modules package provides for the dynamic modification of 
    a user's environment via modulefiles.


    Modules are useful in managing different versions of applications. Modules 
    can also be bundled into meta-modules that will load an entire suite of 
    different applications."""

    homepage = "https://chipsalliance.github.io/verible"
    url = "https://github.com/chipsalliance/verible/archive/refs/tags/v0.0-3428-gcfcbb82b.tar.gz"

    version("v0.0-3428-gcfcbb82b", sha256="3a8e5aaeb81bf11f2c97f28fce49175989aab0cbeda859107d1fbdb054d039f8")

#     version("master", preferred=True)

    depends_on("flex", type="build")
    depends_on("bison", type="build")
    depends_on("bazel%gcc@12.3.0", type="build")

    maintainers("davekeeshan")

    def install(self, spec, prefix):
        #bazel("sync")
        bazel("build", "-c", "opt", "//...")
        bazel("run", "-c", "opt", ":install", "--", prefix.bin)
#         install_tree("bazel-bin", prefix.lib)
# 		bazel run -c opt :install -- ${VERIBLE_INSTALL}/bin
