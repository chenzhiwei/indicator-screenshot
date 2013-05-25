#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 CHENZHIWEI.CN
#
# Author: Chen, Zhi Wei <zhiweik@gmail.com>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3 or any later
# version, as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the applicable version of the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of both the GNU Lesser General Public
# License version 3 and version 2.1 along with this program.  If not, see
# <http://www.gnu.org/licenses>
#

from distutils.core import setup

def main():
    # Default data files
    data_files = [('/usr/share/applications', ['indicator-screenshot.desktop']),
                  ('icons', ['icons/*.png'])]

    setup(name='indicator-screenshot',
            version='0.0.1',
            description='Screenshot Indicator',
            author='Chen, Zhi Wei',
            author_email='zhiweik@gmail.com',
            url='https://github.com/chenzhiwei/indicator-screenshot',
            packages=['indicator-screenshot'],
            data_files=data_files,
            long_description="Indicator Screenshot Integrated"
            "with deepin-screenshot."
         )

if __name__ == "__main__":
    # TODO many things
    main()
