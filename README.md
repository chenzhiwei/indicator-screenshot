# Indicator Screenshot

A simple Ubuntu indicator that integrated with Deepin Screenshot package.

## Install Deepin Screenshot

```
$ cd /tmp
$ wget http://packages.linuxdeepin.com/deepin/pool/main/d/deepin-gsettings/python-deepin-gsettings_0.1+git20130318115600_amd64.deb
$ wget http://packages.linuxdeepin.com/deepin/pool/main/d/deepin-utils/python-deepin-utils_0.0.1-1+git20130506134313_amd64.deb
$ wget http://packages.linuxdeepin.com/deepin/pool/main/d/deepin-ui/deepin-ui_1+git20130522104041_all.deb
$ wget http://packages.linuxdeepin.com/deepin/pool/main/d/deepin-screenshot/deepin-screenshot_2.0%2bgit20131108165119~32e91fbc03_all.deb
$ sudo dpkg -i *.deb
$ sudo apt-get -f install
```

## Install From Source

```
$ cd /tmp
$ git clone git://github.com/chenzhiwei/indicator-screenshot.git
$ cd indicator-screenshot
$ sudo python setup.py install
```

## Install From Ubuntu PPA

```
$ sudo add-apt-repository ppa:chenzhiwei/ppa
$ sudo apt-get update
$ sudo apt-get install indicator-screenshot
```

## Make it auto start

```
$ cp /usr/share/indicator-screenshot/indicator-screenshot.desktop ~/.config/autostart
```

## Git Repository

* Origin repo: <https://github.com/chenzhiwei/indicator-screenshot>
* Backup repo: <https://gitshell.com/chenzhiwei/indicator-screenshot>
