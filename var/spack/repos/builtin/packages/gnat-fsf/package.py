# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class GnatFsf(Package):
    """The GNAT Ada compiler. Ada is a modern programming language designed
    for large, long-lived applications - and embedded systems in particular
    - where reliability and efficiency are essential."""

    homepage = "https://libre.adacore.com/tools/gnat-gpl-edition/"

    # NOTE: This is a binary installer intended to bootstrap GCC's Ada compiler

    # There may actually be a way to install GNAT from source. If you go to
    # the GNAT Download page: https://libre.adacore.com/download/
    # select "Free Software or Academic Development", select your platform,
    # expand GNAT Ada, and expand Sources, you'll see links to download the
    # source code for GNAT and all of its dependencies. Most of these
    # dependencies are already in Spack.

    # This is the GPL release for Linux x86-64
    version(
        "12.2.0.1",
        sha256="11f3b811e4967bd4924a8236e9e68e0b9464fee016cd9d00c077faec0c27fe99",
        url="https://github.com/alire-project/GNAT-FSF-builds/releases/download/gnat-12.2.0-1/gnat-x86_64-linux-12.2.0-1.tar.gz",
    )
    def install(self, spec, prefix):
        install_tree(".", prefix)
