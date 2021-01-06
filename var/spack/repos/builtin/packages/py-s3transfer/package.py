# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyS3transfer(PythonPackage):
    """S3transfer is a Python library for managing Amazon S3 transfers."""

    homepage = "https://github.com/boto/s3transfer"
    pypi = "s3transfer/s3transfer-0.3.3.tar.gz"

    version('0.3.3', sha256='921a37e2aefc64145e7b73d50c71bb4f26f46e4c9f414dc648c6245ff92cf7db')
    version('0.2.1', sha256='6efc926738a3cd576c2a79725fed9afde92378aa5c6a957e3af010cb019fac9d')

    depends_on('py-setuptools', type='build')
    depends_on('py-botocore@2.0.0:', when='@0.3.0:0.3.999', type=('build', 'run'))
    depends_on('py-botocore@1.12.36:1.999', when='@0.2.0:0.2.999', type=('build', 'run'))
    depends_on('py-futures@2.2:3', type=('build', 'run'), when='^python@:2')
