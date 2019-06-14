#!/usr/bin/env python

import os
from setuptools import setup, find_packages


here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read().strip()

setup(
    name='{{cookiecutter.github_repository_name}}',
    version='0.1.0',
    author='{{cookiecutter.github_username}}',
    author_email='{{cookiecutter.email}}',
    url='http://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}',
    license='Apache License 2.0',
    description='''
    {{cookiecutter.description}}
    ''',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='''
    django rest auth registration rest-framework django-registration api
    ''',
    zip_safe=False,
    include_package_data=True,
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django :: 2.2',
        'License :: OSI Approved :: Apache License, Version 2.0 (Apache-2.0)',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP'
    ],
)
