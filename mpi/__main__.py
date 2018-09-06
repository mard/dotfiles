#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('mpv')

FileInstaller.create_symlink(os.path.join(dir, 'config'), '~/.config/mpi')
FileInstaller.create_symlink(os.path.join(dir, 'mpi'), '~/scripts/bin/mpi')
FileInstaller.create_symlink(os.path.join(dir, 'mpi.desktop'), '~/.local/share/applications/mpi.desktop')
