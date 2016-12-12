#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller, run_verbose
dir = os.path.dirname(__file__)

FileInstaller.create_symlink(os.path.join(dir, 'xinitrc'), '~/.xinitrc')
FileInstaller.create_symlink(os.path.join(dir, 'Xresources'), '~/.config/Xresources')
FileInstaller.create_symlink(os.path.join(dir, 'imwheelrc'), '~/.imwheelrc')
run_verbose(['xrdb', os.path.expanduser('~/.config/Xresources')])

