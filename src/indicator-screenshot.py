#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 CHENZHIWEI.CN
#
# Author: Chen Zhiwei <zhiweik@gmail.com>
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

import os,gtk 
import appindicator
import pynotify
import dbus

class IndicatorScreenshot:
    def __init__(self, args = None):
        if dbus.SessionBus().request_name("cn.chenzhiwei.indicator-screenshot")\
                != dbus.bus.REQUEST_NAME_REPLY_PRIMARY_OWNER:
            exit("IndicatorScreenshot Already Running!")

        self.args = args
        # Create App Indicator
        self.ind = appindicator.Indicator(
                "Indicator Screenshot", "indicator-screenshot",
                appindicator.CATEGORY_APPLICATION_STATUS)

        realpath = os.path.realpath(__file__)
        self.ind.set_icon_theme_path(os.path.abspath(os.path.join(
                os.path.dirname(realpath), 'icons')))
        self.ind.set_icon("indicator")
        self.ind.set_status(appindicator.STATUS_ACTIVE)

        # Create Menu
        self.menu = gtk.Menu()
        self.mSelectArea= gtk.MenuItem("Select Area")
        self.menu.append(self.mSelectArea)
        self.mSelectArea.connect("activate", self.select_area, None)
        self.mSelectArea.show()

        self.mFullScreen = gtk.MenuItem("Full Screen")
        self.menu.append(self.mFullScreen)
        self.mFullScreen.connect("activate", self.full_screen, None)
        self.mFullScreen.show()

        self.exit = gtk.MenuItem("Exit")
        self.menu.append(self.exit)
        self.exit.connect("activate", self.exit_indicator, None)
        self.exit.show()

        # Connect Indicator to menu
        self.ind.set_menu(self.menu)

    def exit_indicator(self, *args):
        exit(0)

    def select_area(self, *args):
        os.system('deepin-screenshot')
        realpath = os.path.realpath(__file__)
        uri = "file://" + os.path.abspath(os.path.dirname(realpath)) \
                + "/icons/screenshot-notification.svg"
        title = 'Screenshot Complete'
        content = 'File saved to `~/Pictures` directory.'
        self.show_notification(title, content, uri)

    def full_screen(self, *args):
        os.system('deepin-screenshot -f')
        realpath = os.path.realpath(__file__)
        uri = "file://" + os.path.abspath(os.path.dirname(realpath)) \
                + "/icons/screenshot-notification.svg"
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
    gtk.main()
    exit(0)

if __name__ == "__main__":
    main()
