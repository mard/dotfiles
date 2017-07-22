#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('gzdoom')
FileInstaller.create_symlink(os.path.join(dir, 'gzdoom.ini'), '~/.config/gzdoom/gzdoom.ini')

