#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   setup.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

VERSION = '1.0'

from setuptools import (
    setup,
)

if __name__ == '__main__':
    setup(
        name='html-table',
        version=VERSION,
        author='Fasion Chan',
        author_email='fasionchan@gmail.com',
        packages=[
            'HTMLTable',
        ],
    )
