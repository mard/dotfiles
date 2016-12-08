#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('xorg-server')
PackageInstaller.try_install('xorg-xinit')
PackageInstaller.try_install('xorg-xrandr')
PackageInstaller.try_install('xdotool')
PackageInstaller.try_install('pkg-config')

FileInstaller.create_symlink(os.path.join(dir, 'xinitrc'), '~/.xinitrc')
FileInstaller.create_symlink(os.path.join(dir, 'Xresources'), '~/.config/Xresources')
run_verbose(['xrdb', os.path.expanduser('~/.config/Xresources')])

