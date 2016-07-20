#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('slock')

FileInstaller.create_symlink(os.path.join(dir, 'bin'), '~/scripts/bin')
FileInstaller.create_symlink(os.path.join(dir, 'lib'), '~/scripts/lib')

