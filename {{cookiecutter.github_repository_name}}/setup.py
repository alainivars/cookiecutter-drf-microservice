#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from utils2devops.tools.single_sourcing_package_version import get_version

version = get_version('.')

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read().strip()

setup(
    name='{{cookiecutter.github_repository_name}}',
    version=version,
    author='{{cookiecutter.github_username}}',
    author_email='{{cookiecutter.email}}',
    url='http://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}',
    license='Apache License 2.0',
    description='''
    {{cookiecutter.description}}.
    Read the README.rst for more information.
    ''',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/x-rst',
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
        'Topic :: Internet :: WWW/HTTP'
    ],
)
