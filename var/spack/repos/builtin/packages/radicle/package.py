# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Radicle(Package):
    """Radicle Heartwood Protocol & Stack

    Heartwood is the third iteration of the Radicle Protocol, a powerful 
    peer-to-peer code collaboration and publishing stack. The repository contains 
    a full implemention of Heartwood, complete with a user-friendly command-line 
    interface (rad) and network daemon (radicle-node).

    Radicle was designed to be a secure, decentralized and powerful alternative 
    to code forges such as GitHub and GitLab that preserves user sovereignty 
    and freedom.
    """

    homepage = "https://radicle.xyz/"
    git = "https://seed.radicle.xyz/z3gqcJUoA1n9HaHKufZs5FCSGazv5.git"

    maintainers("davekeeshan")

    license("MIT")

    version("master", branch="master")
#     version("0.8.0", commit="f15afa84be7bda050bfb93e321bbce28b56d10b6")
    version("0.8.0", commit="f15afa8")


    depends_on("git", type=("build", "run"))
    depends_on("openssh", type="build")
    depends_on("rust", type="build")

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("install", "--root", prefix, "--path", "radicle-cli",  "--force", "--locked")
        cargo("install", "--root", prefix, "--path", "radicle-node",  "--force", "--locked")
        cargo("install", "--root", prefix, "--path", "radicle-remote-helper",  "--force", "--locked")
