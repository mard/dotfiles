#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller, run_verbose
dir = os.path.dirname(__file__)

FileInstaller.create_symlink(os.path.join(dir, 'xinitrc'), '~/.xinitrc')
FileInstaller.create_symlink(os.path.join(dir, 'Xresources'), '~/.Xresources')
FileInstaller.create_symlink(os.path.join(dir, 'imwheelrc'), '~/.imwheelrc')
run_verbose(['xrdb', '-merge', os.path.expanduser('~/.Xresources')])
