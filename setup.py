import os

import setuptools
from setuptools import setup

from tcsdk.common import default

PACKAGE_NAME = default.NAME

requires = [
    'requests',
    'setuptools',
]

with open('README.md', mode='r') as f:
    long_description = f.read()


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


package_extras = []

package_extras.extend(package_files('{}/common'.format(PACKAGE_NAME)))
package_extras.extend(package_files('{}/network'.format(PACKAGE_NAME)))

setup(
    name=default.NAME,
    version=default.TCSDK_VERSION,
    author='wei.meng',
    author_email='mengwei1101@hotmail.com',
    description="tcloud sdk for upload data!",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/tsbxmw/tcsdk',
    packages=setuptools.find_packages(exclude=['tests']),
    package_data={"": package_extras},
    install_requires=requires,
    platforms='Posix; MacOS X; Windows',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)
