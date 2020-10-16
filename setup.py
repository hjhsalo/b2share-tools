#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    # 'Click>=6.0',
    # 'invenio-db[postgresql,versioning]>=1.0.0b8',
    # 'invenio-pidstore>=v1.0.0b2',
    # 'invenio-records-files>=1.0.0a9',
    # 'psycopg2>=2.6.1',
    # 'SQLAlchemy-Utils<0.35,>=0.33.1',
    'b2share>=2.1.0'
]

setup(
    name='b2share-tools',
    version='0.1.0',
    description="B2SHARE cli administrative commands",
    long_description=readme,
    author="Harri Hirvonsalo",
    author_email='',
    url='',
    packages=find_packages(include=['b2share-tools']),
    entry_points={
        'invenio_base.api_apps': [
            'b2share_tools = b2share_tools:B2ShareTools',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='b2share-tools',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ]
)
