# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Verible(Package):
    """The Verible project’s main mission is to parse SystemVerilog 
    (IEEE 1800-2017) (as standardized in the [SV-LRM]) for a wide variety of 
    applications, including developer tools.

    It was born out of a need to parse un-preprocessed source files, which is 
    suitable for single-file applications like style-linting and formatting. 
    In doing so, it can be adapted to parse preprocessed source files, which 
    is what real compilers and toolchains require.

    The spirit of the project is that no-one should ever have to develop a 
    SystemVerilog parser for their own application, because developing a 
    standard-compliant parser is an enormous task due to the syntactic 
    complexity of the language. Verible’s parser is also regularly tested 
    against an ever-growing suite of (tool-independent) language compliance 
    tests at https://symbiflow.github.io/sv-tests/.

    A lesser (but notable) objective is that the language-agnostic components 
    of Verible be usable for rapidly developing language support tools for 
    other languages."""

    homepage = "https://chipsalliance.github.io/verible"
    #url = "https://github.com/chipsalliance/verible/archive/refs/tags/v0.0-3428-gcfcbb82b.tar.gz"

    version("v0.0-3428-gcfcbb82b", sha256="3a8e5aaeb81bf11f2c97f28fce49175989aab0cbeda859107d1fbdb054d039f8", url = "https://github.com/chipsalliance/verible/archive/refs/tags/v0.0-3428-gcfcbb82b.tar.gz")

    maintainers("davekeeshan")
#     version("master", preferred=True)

    depends_on("flex")
    depends_on("bison")
    depends_on("bazel", type="build")

    def install(self, spec, prefix):
        bazel("build", "-c", "opt", "//...")
        bazel("run", "-c", "opt", ":install", "--", prefix.bin)
