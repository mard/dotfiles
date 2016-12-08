#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

FileInstaller.create_symlink(os.path.join(dir, 'locale.conf'), '~/.config/locale.conf')
FileInstaller.create_symlink(os.path.join(dir, 'user-dirs.dirs'), '~/.config/user-dirs.dirs')

