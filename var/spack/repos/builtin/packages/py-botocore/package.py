# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyBotocore(PythonPackage):
    """Low-level, data-driven core of boto 3."""

    homepage = "https://github.com/boto/botocore"
    pypi = "botocore/botocore-1.13.44.tar.gz"

    version('2.0.0dev83', sha256='26d1af9607bc0f287ae548827c151c62517815435f90253b90b49f176c5b8903',
        url="https://github.com/boto/botocore/archive/717935472d7743be9cd170a6127a2a6c52d19c09.tar.gz")
    version('1.13.44',  sha256='a4409008c32a3305b9c469c5cc92edb5b79d6fcbf6f56fe126886b545f0a4f3f')
    version('1.13.38',  sha256='15766a367f39dba9de3c6296aaa7da31030f08a0117fd12685e7df682d8acee2')
    version('1.12.169', sha256='25b44c3253b5ed1c9093efb57ffca440c5099a2d62fa793e8b6c52e72f54b01e')

    depends_on('py-setuptools', type='build')
    depends_on('py-jmespath@0.7.1:0.999', type=('build', 'run'))
    #depends_on('py-docutils@0.10:0.15', type=('build', 'run'))
    #depends_on('py-ordereddict@1.1', type=('build', 'run'), when='^python@2.6.0:2.6.999')
    #depends_on('py-simplejson@3.3.0', type=('build', 'run'), when='^python@2.6.0:2.6.999')
    depends_on('py-python-dateutil@2.1:2.999', type=('build', 'run'))
    #depends_on('py-python-dateutil@2.1:2.6', type=('build', 'run'), when='^python@2.6.0:2.6.999')
    depends_on('py-urllib3@1.25.4:1.26.999', type=('build', 'run'), when='@2.0.0dev82:')
    depends_on('py-urllib3@1.20:1.25', type=('build', 'run'), when='@1.12.169:1.13.44')
    #depends_on('py-urllib3@1.20:1.23', type=('build', 'run'), when='^python@2.6.0:2.6.999')
    #depends_on('py-urllib3@1.20:1.22', type=('build', 'run'), when='^python@3.3.0:3.3.999')
