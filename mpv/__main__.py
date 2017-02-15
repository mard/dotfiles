#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('mpv')
FileInstaller.create_symlink(os.path.join(dir, 'mpv.conf'), '~/.config/mpv/mpv.conf')
FileInstaller.create_symlink(os.path.join(dir, 'input.conf'), '~/.config/mpv/input.conf')

