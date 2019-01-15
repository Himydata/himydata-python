#!/usr/bin/env python

from setuptools import setup

VERSION = "0.0.1"

long_description = (open('README.md').read() +
    '\n\n' + open('HISTORY.txt').read())

setup(
        name='himydata-library',
        version=VERSION,
        license="Apache Software License",
        packages=["himydata", "himydata.utils", "himydata.hmd", "himydata.hmd.api"],
        description="Python library for Himydata Platform",
        long_description=long_description,
        author="Himydata",
        author_email="support@himydata.com",
        url="https://www.himydata.com",
        classifiers = [
            'Development Status :: 0.1 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Topic :: Software Development :: Libraries',
            'Programming Language :: Python',
            'Operating System :: OS Independent'
        ],
        install_requires = [
            "requests>=2.19.1",
            "python-dateutil",
            "cassandra-driver>=3.13.0",
            "numpy",
            "SQLAlchemy"
        ]
     )
