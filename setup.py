#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'cliff',
    'datakit-core',
    'requests'
]

test_requirements = [
    'pytest'
]

setup(
    name='datakit-dworld',
    version='0.1.0',
    description="Commands to manage project integration with data.world.",
    long_description=readme + '\n\n' + history,
    author="Justin Myers",
    author_email='jmyers@ap.org',
    url='https://github.com/associatedpress/datakit-dworld',
    packages=[
        'datakit_dworld',
    ],
    package_dir={'datakit_dworld':
                 'datakit_dworld'},
    include_package_data=True,
    entry_points={
        'datakit.plugins': [
            'dworld:create= datakit_dworld.create:Create',
            'dworld:push= datakit_dworld.push:Push',
        ]
    },
    install_requires=requirements,
    license="ISC license",
    zip_safe=False,
    keywords='datakit-dworld',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
