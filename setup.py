#!/usr/bin/env python

from setuptools import setup

VERSION = "0.0.1"

long_description = (open('README.md').read() +
                    '\n\n' + open('HISTORY.txt').read())

setup(
    name='himydata-library',
    version=VERSION,
    license="Apache Software License",
    packages=["himydata", "himydata.utils", "himydata.hmd", "himydata.hmd.api", "himydata.hmd.utils"],
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
    install_requires=[
        "requests",
        "python-dateutil",
        "cassandra-driver",
        "numpy",
        "pandas",
        "sqlalchemy",
        "psycopg2>=2.7.5",
        "psycopg2-binary>=2.7.5"
    ]
)
