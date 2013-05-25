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

import gtk 
import appindicator
import pynotify
import os

class IndicatorScreenshot:
    def __init__(self, args = None):
        self.args = args
        # Create App Indicator
        self.ind = appindicator.Indicator(
                "Indicator Screenshot", "indicator-screenshot",
                appindicator.CATEGORY_APPLICATION_STATUS)
        # Delete/modify the following file when distributing as a package
        self.ind.set_icon_theme_path(os.path.abspath(os.path.join(
            os.path.dirname(__file__), 'icons')))
        self.ind.set_icon("ubuntu-logo-16")
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        # Create Menu
        self.menu = gtk.Menu()
        self.mSelectArea= gtk.MenuItem("Select Area")
        self.menu.append(self.mSelectArea)
        self.mSelectArea.connect("activate", self.select_area, None)
        self.mSelectArea.show()

        self.mFullScreen= gtk.MenuItem("Full Screen")
        self.menu.append(self.mFullScreen)
        self.mFullScreen.connect("activate", self.full_screen, None)
        self.mFullScreen.show()

        # Connect Indicator to menu
        self.ind.set_menu(self.menu)

    def select_area(self, *args):
        os.system('deepin-screenshot')
        uri = "file://" + os.path.abspath(os.path.dirname(__file__)) + "/icons/ubuntu-logo-48.svg"
        title = 'Screenshot Complete'
        content = 'This is a notification from indicator-screenshot.'
        self.show_notification(title, content, uri)

    def full_screen(self, *args):
        os.system('deepin-screenshot -f')
        uri = "file://" + os.path.abspath(os.path.dirname(__file__)) + "/icons/ubuntu-logo-48.svg"
        title = 'Screenshot Complete'
        content = 'This is a notification from indicator-screenshot.'
        self.show_notification(title, content, uri)

    def show_notification(self, title, content, icon):
        if not pynotify.init("icon-summary-body"):
            exit(1)

        n = pynotify.Notification(title, content, icon)
        n.show()

def main():
    args = None

    indicator = IndicatorScreenshot(args)
    # Load global css for the first time.
    gtk.main()

if __name__ == "__main__":
    main()
