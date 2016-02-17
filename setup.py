import os
import re

import pkg_resources
from setuptools import setup, find_packages


def read_version(fobj):
    regex = re.compile(r'^__version__\s*=\s*u?[\'"]([^\'"]+)')
    for line in fobj:
        matches = regex.match(line)
        if matches:
            return matches.group(1)

    # Else unknown version
    return 'unknown'
    

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'pyuserdb', '__init__.py')) as f:
    module_version = read_version(f)

with open(os.path.join(HERE, 'README.rst')) as f:
    README = f.read()

with open(os.path.join(HERE, 'CHANGES.rst')) as f:
    CHANGES = f.read()

with open(os.path.join(HERE, 'requirements.txt')) as f:
    requires = map(str, pkg_resources.parse_requirements(f.read()))


setup(
    name='pyuserdb',
    version=module_version,
    description='pyuserdb',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
    ],
    author='',
    author_email='',
    url='',
    keywords='cassandra',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite='pyuserdb',
    entry_points={
        'console_scripts': [
            'pyuserdb_sync_tables = pyuserdb.scripts.sync_tables:main',
        ],
    }
)
