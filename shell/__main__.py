#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('bash')
FileInstaller.create_symlink(os.path.join(dir, 'bash_profile'), '~/.bash_profile')
FileInstaller.create_symlink(os.path.join(dir, 'bashrc'), '~/.bashrc')
FileInstaller.create_symlink(os.path.join(dir, 'inputrc'), '~/.inputrc')
FileInstaller.create_symlink(os.path.join(dir, 'locale.conf'), '~/.config/locale.conf')
