#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('code')

FileInstaller.create_symlink(os.path.join(dir, 'settings.json'), '~/.config/Code/User/settings.json')
FileInstaller.create_symlink(os.path.join(dir, 'settings.json'), '~/.config/Code - OSS/User/settings.json')
