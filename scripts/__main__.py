#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('slock')

FileInstaller.create_symlink(os.path.join(dir, 'bin/a73'), '~/scripts/bin/a73')
FileInstaller.create_symlink(os.path.join(dir, 'bin/util'), '~/scripts/bin/util')
FileInstaller.create_symlink(os.path.join(dir, 'lib'), '~/scripts/lib')

