#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('redshift')

FileInstaller.create_symlink(os.path.join(dir, 'redshift.conf'), '~/.config/redshift.conf')