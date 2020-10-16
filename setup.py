#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=6.0',
    'invenio-db[postgresql,versioning]==1.0.0b8',
    'invenio-pidstore==v1.0.0b2',
    'invenio-records-files==1.0.0a9',
    'psycopg2>=2.6.1',
    'SQLAlchemy-Utils<0.36,>=0.33.1'
    # 'psycopg2-binary'
]

setup(
    name='b2tools',
    version='0.1.0',
    description="B2SHARE cli administrative commands",
    long_description=readme,
    author="Harri Hirvonsalo",
    author_email='',
    url='https://github.com/travishathaway/click-boilerplate',
    packages=find_packages(include=['b2tools']),
    entry_points={
        # ATTENTION! ACHTUNG! ATENCIÓN!
        # 
        # The following lines determine what your CLI program is 
        # called and where it will look for it. Please edit to suit
        # your needs
        'console_scripts': [
            'b2tools=cli_app:cli'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='b2tools',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ]
)
