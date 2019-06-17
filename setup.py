#!/usr/bin/env python

import os
import re
from setuptools import setup, find_packages


def read(f):  # todo: move to util2devops lib, from DRF setup
    return open(f, 'r', encoding='utf-8').read()


def get_version(package):  # todo: move to util2devops lib, from DRF setup
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, 'version.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('.')

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read().strip()

setup(
    name='cookiecutter-drf-microservice',
    version=version,
    author='Alain IVARS',
    author_email='alainivars@gmail.com',
    url='http://github.com/alainivars/cookiecutter-drf-microservice',
    license='Apache License 2.0',
    description='''
    Create a REST API endpoints with Authentication and Registration.
    Read the README.rst for more information.
    ''',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='''
    django rest auth registration rest-framework django-registration api docker cookiecuter tox pytest
    ''',
    zip_safe=False,
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP'
    ],
)
