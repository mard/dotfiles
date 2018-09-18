#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller, run_verbose
dir = os.path.dirname(__file__)

PackageInstaller.try_install('xorg-server')
PackageInstaller.try_install('xorg-xinit')
PackageInstaller.try_install('xorg-xset')
PackageInstaller.try_install('xorg-xrdb')

FileInstaller.create_symlink(os.path.join(dir, 'xinitrc'), '~/.xinitrc')
FileInstaller.create_symlink(os.path.join(dir, 'Xresources'), '~/.Xresources')
FileInstaller.create_symlink(os.path.join(dir, 'imwheelrc'), '~/.imwheelrc')
run_verbose(['xrdb', '-merge', os.path.expanduser('~/.Xresources')])
