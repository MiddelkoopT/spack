# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyS3transfer(PythonPackage):
    """S3transfer is a Python library for managing Amazon S3 transfers."""

    homepage = "https://github.com/boto/s3transfer"
    url      = "https://github.com/boto/s3transfer/archive/0.3.3.tar.gz"

    version('0.3.3', sha256='0c8b0f7aaf32173d1475df0a453bfdc37be8207ea15c1d8415a590ef3986fc51')
    version('0.2.1', sha256='6efc926738a3cd576c2a79725fed9afde92378aa5c6a957e3af010cb019fac9d')

    depends_on('py-setuptools', type='build')
    depends_on('py-botocore@2.0.0:', when='@0.3.0:0.3.999', type=('build', 'run'))
    depends_on('py-botocore@1.12.36:1.999', when='@0.2.0:0.2.999', type=('build', 'run'))
    depends_on('py-futures@2.2:3', type=('build', 'run'), when='^python@:2')
