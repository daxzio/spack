# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os
from glob import glob
from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class ArmGnuToolchain(Package):
    """Arm GNU Toolchain is a community supported pre-built GNU compiler toolchain for Arm based CPUs."""

    homepage = "https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads"
    url = "https://developer.arm.com/-/media/Files/downloads/gnu/13.2.rel1/binrel/arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz"

    maintainers("davekeeshan")

    version(
        "14.2.rel1",
        url="https://developer.arm.com/-/media/Files/downloads/gnu/14.2.rel1/binrel/arm-gnu-toolchain-14.2.rel1-x86_64-arm-none-eabi.tar.xz",
        sha256="62a63b981fe391a9cbad7ef51b17e49aeaa3e7b0d029b36ca1e9c3b2a9b78823",
    )
    version(
        "13.3.rel1",
        url="https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz",
        sha256="95c011cee430e64dd6087c75c800f04b9c49832cc1000127a92a97f9c8d83af4",
    )
    version(
        "13.2.rel1",
        url="https://developer.arm.com/-/media/Files/downloads/gnu/13.2.rel1/binrel/arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz",
        sha256="6cd1bbc1d9ae57312bcd169ae283153a9572bd6a8e4eeae2fedfbc33b115fdbb",
    )
    
#     depends_on("python@3.9:")
    
    def install(self, spec, prefix):
        src = os.getcwd()
        content = glob(f"{src}/*")
        mv = which("mv")
        for c in content:
            mv("-if", c, prefix)

#https://developer.arm.com/-/media/Files/downloads/gnu/13.2.rel1/srcrel/arm-gnu-toolchain-src-snapshot-13.2.rel1.tar.xz
