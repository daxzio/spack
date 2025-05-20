# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Openfpgaloader(CMakePackage):
    """openFPGALoader is a universal utility for programming FPGAs. Compatible 
    with many boards, cables and FPGA from major manufacturers (Xilinx, 
    Altera/Intel, Lattice, Gowin, Efinix, Anlogic, Cologne Chip). 
    openFPGALoader works on Linux, Windows and macOS."""

    homepage = "https://trabucayre.github.io/openFPGALoader/"
    url = "https://github.com/trabucayre/openFPGALoader/archive/refs/tags/v0.12.1.tar.gz"
    git = "https://github.com/trabucayre/openFPGALoader.git"

    maintainers("davekeeshan")

    license("Apache-2.0 OR MIT")

    version("master", branch="master")
    version("0.13.1", sha256="372f1942dec8a088bc7475f94ccf5a86264cb74e9154d8a162b8d4d26d3971e3")
    version("0.13.0", sha256="f8037b8080eec21afc74284c8b0352a2ba76ea685733ba63d8322d6fe39e7721")
    version("0.12.1", sha256="8fb2d1aa3a0de50222f6286c47220a5bc7b73708b60fb7d58f764deebd43d82d")

    variant("linuxgpiod", default=True, description="build with linux gpio support")
#     depends_on("c", type="build")
#     depends_on("cxx", type="build")

#     depends_on("libudev", type="build")
#     depends_on("zlib", type="build")
#     depends_on("pkgconfig", type="build")
    depends_on("libusb", type="build")
    depends_on("libftdi", type="build")
    depends_on("libgpiod@:1.6", type="build", when="+linuxgpiod")
#     depends_on("systemd")  # For libuvdev

#     def setup_dependent_build_environment(
#         self, env: EnvironmentModifications, dependent_spec: Spec
#     ) -> None:
#         env.prepend_path("PKG_CONFIG_PATH", join_path(self.prefix, "rlib", "pkgconfig"))

    def setup_run_environment(self, env):
        env.prepend_path("OPENFPGALOADER_SOJ_DIR", f"{self.prefix}/share/openFPGALoader")

#     def build(self, spec, prefix):
#         build_dir = "build"
#         with working_dir(build_dir, create=True):
#             cmake("..")

#     @run_before("install")
#     def cmake(self):
#         cmake = which("cmake")
# 
#         build_dir = "build"
# 
#         with working_dir(build_dir, create=True):
#             cmake("..")
#             cmake("--build .")
# 
#     # CMake options
#     def cmake_args(self):
#         spec = self.spec
# 
#         args = [
#             self.define("BUILD_TESTING", self.run_tests),
#             self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
#             self.define_from_variant("BUILD_UTILITIES", "utilities"),
#             self.define_from_variant("BUILD_CFP", "c"),
#             self.define_from_variant("BUILD_ZFPY", "python"),
#             self.define_from_variant("BUILD_ZFORP", "fortran"),
#             self.define_from_variant("ZFP_WITH_OPENMP", "openmp"),
#             self.define_from_variant("ZFP_WITH_CUDA", "cuda"),
#             self.define_from_variant("ZFP_WITH_ALIGNED_ALLOC", "aligned"),
#             self.define("ZFP_BIT_STREAM_WORD_SIZE", spec.variants["bsws"].value),
#             self.define_from_variant("ZFP_WITH_DAZ", "daz"),
#             self.define_from_variant("ZFP_WITH_CACHE_FAST_HASH", "fasthash"),
#             self.define_from_variant("ZFP_WITH_CACHE_PROFILE", "profile"),
#             self.define_from_variant("ZFP_WITH_BIT_STREAM_STRIDED", "strided"),
#             self.define_from_variant("ZFP_WITH_TIGHT_ERROR", "tight-error"),
#             self.define_from_variant("ZFP_WITH_CACHE_TWOWAY", "twoway"),
#         ]
# 
#         if "round" in spec.variants:
#             args.append(
#                 "ZFP_ROUNDING_MODE=ZFP_ROUND_{0}".format(spec.variants["round"].value.upper())
#             )
# 
#         if "+cuda" in spec:
#             args.append("-DCUDA_BIN_DIR={0}".format(spec["cuda"].prefix.bin))
# 
#             if not spec.satisfies("cuda_arch=none"):
#                 cuda_arch = spec.variants["cuda_arch"].value
#                 args.append("-DCMAKE_CUDA_FLAGS=-arch sm_{0}".format(cuda_arch[0]))
# 
#         return args
