# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import shlex
from subprocess import Popen

from spack.package import *


class RiscvGnuToolchain(AutotoolsPackage):
    """A cross-compilation tool for RISC-V."""

    homepage = "https://riscv.org"
    git = "https://github.com/riscv-collab/riscv-gnu-toolchain.git"

    maintainers("wanlinwang")

    version("develop", branch="master", submodules=True)
    version(
        "2023.10.18",
        tag="2023.10.18",
        commit="b86b2b37d0acc607156ff56ff17ee105a9b48897",
        submodules=True,
    )
    version(
        "2023.01.04",
        tag="2023.01.04",
        commit="51c73700789f54db7e8c22e5bf1654bcfdd074d0",
        submodules=True,
    )
        "2023.10.17",
        tag="2023.10.17",
        commit="c11f0748276c58df4f9d9602cdc2de5f17cbae8c",
        submodules=True,
    )
    version(
        "2023.10.12",
        tag="2023.10.12",
        commit="e65e7fc58543c821baf4f1fb6d0ef700177b9d89",
        submodules=True,
    )
    version(
        "2023.10.06",
        tag="2023.10.06",
        commit="6e7190e8c95e09d541e69f6f6e39163f808570d5",
        submodules=True,
    )
    version(
        "2023.09.27",
        tag="2023.09.27",
        commit="5afde2de23c6597aaa5069f36574c61bcb39b007",
        submodules=True,
    )
    version(
        "2023.09.26",
        tag="2023.09.26",
        commit="ffb5968884630c7baebba7b2af493f6b5f74ad80",
        submodules=True,
    )
    version(
        "2023.09.13",
        tag="2023.09.13",
        commit="5437780994b830e9eabf467f85f22ed24b5fade1",
        submodules=True,
    )
    version(
        "2022.08.08",
        tag="2022.08.08",
        commit="cb25bb862a3bf56d1577d7930bc41f259632ae24",
        submodules=True,
    )
#     version(
#         "2018.06.29",
#         tag="v20180629",
#         commit="cb6b34b8581bfc72197aa24bd4f367d54db81b51",
#         submodules=True,
#     )
    version(
        "2018.02.14",
        tag="v20180629",
        commit="411d134",
        submodules=True,
    )

    variant("32", default=False, description="32 bit only support")
    variant("multilib", default=False, description="64 and 32 bit support")

    variant(
        "rvarch",
        default="rv32gc",
        values=("rv32i", "rv32ic", "rv32im", "rv32imc", "rv32gc"),
        description="Different compiler setting",
    )

    variant(
        "compiler_type",
        default="newlib",
        values=("newlib", "linux"),
        description="Compiler back-end to build",
    )

    # Dependencies:
    depends_on("pkgconfig", type="build")
    depends_on("autoconf", when="@main:", type="build")
    depends_on("python", type="build")
    depends_on("gawk", type="build")
    depends_on("bison", type="build")
    depends_on("flex@:2.6.1,2.6.4:", type="build")
    depends_on("texinfo", type="build")
    depends_on("patchutils", type="build")
    depends_on("mpc", type="build")
    depends_on("gmp", type="build")
    depends_on("mpfr", type="build")
    depends_on("zlib-api", type=("build", "link"))
    depends_on("expat", type=("build", "link"))
    depends_on("bzip2", type="build")
    depends_on("gmake@4.3:", type="build")

    conflicts("platform=windows", msg="Windows is not supported.")

    def configure_args(self):
        self.spec.prefix = f"{prefix}-rv32i"
        args = []
#         args += self.with_or_without("arch=rv32gc", variant="32")    
#         args += self.with_or_without("abi=ilp32d", variant="32")    
    
        if self.spec.satisfies("+32"):
        #if self.spec.satisfies("rvarch=rv32i"):
            args.append("--with-arch=rv32i")

#             args.append("--with-arch=rv32gc")


#      16009    --with-abi=ilp32d is not supported for ISA rv32i
#         if self.spec.satisfies("+32"):
#             args.append("--with-abi=ilp32d")
#         if self.spec.satisfies("+multilib"):
#             args.append("--enable-multilib")
        args += self.enable_or_disable("multilib", variant="multilib")    
        
#         args.append("-xib")
        return args
    
    def build(self, spec, prefix):
        """Makes the build targets specified by
        :py:attr:``~.AutotoolsPackage.build_targets``
        """
        with working_dir(self.stage.source_path):
            # modify Makefile not to git init submodules.
            cmd = "/bin/sed -i.bak -r \
            '/^# Rule for auto init submodules/,/git submodule update.*$/d' \
            Makefile"
            p = Popen(shlex.split(cmd))
            p.wait()
            p.communicate()

            params = []
            if self.spec.satisfies("compiler_type=linux"):
                params.append("linux")

            make(*params)
