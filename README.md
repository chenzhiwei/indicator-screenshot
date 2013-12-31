# Indicator Screenshot

A simple Ubuntu indicator that integrated with Deepin Screenshot package.

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

## Install Deepin Screenshot packages

You MUST first install `indicator-screenshot` from PPA.

```
$ sudo dpkg -i /tmp/deepin/*.deb
$ sudo apt-get install -f
```

## Make it auto start

```
$ cp /usr/share/indicator-screenshot/indicator-screenshot.desktop ~/.config/autostart
```

## Supported platform

Only available on Ubuntu 13.10.

## Git Repository

* Origin repo: <https://github.com/chenzhiwei/indicator-screenshot>
* Backup repo: <https://gitshell.com/chenzhiwei/indicator-screenshot>
