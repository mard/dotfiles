#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('git')
FileInstaller.create_symlink(os.path.join(dir, 'gitconfig'), '~/.gitconfig')
