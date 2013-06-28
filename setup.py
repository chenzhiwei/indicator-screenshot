#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from glob import glob

NAME = 'indicator-screenshot'
DESCRIPTION = 'An indicator for Deepin screenshot'
VERSION = '0.0.1'
AUTHOR = 'Chen Zhiwei'
AUTHOR_EMAIL = 'zhiweik@gmail.com'
URL = 'http://github.com/chenzhiwei/indicator-screenshot'
LICENSE = 'GNU General Public License (GPL)'
DATA_FILES = [('/usr/share/indicator-screenshot/icons', glob('data/icons/*')),
        ('/usr/share/indicator-screenshot', glob('data/*.desktop')),
        ('/usr/share/indicator-screenshot', glob('src/*.py')),
        ('/usr/bin', ['bin/indicator-screenshot']),
        ('/usr/share/applications', ['data/indicator-screenshot.desktop']),
        ('/usr/share/pixmaps', ['data/icons/indicator-screenshot.png'])]

def main():
    setup(name = NAME,
        description = DESCRIPTION,
        version = VERSION,
        author = AUTHOR,
        author_email = AUTHOR_EMAIL,
        url = URL,
        license = LICENSE,
        data_files=DATA_FILES,
        )

if __name__ == '__main__':
    main()
