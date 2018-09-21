#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller, run_verbose
dir = os.path.dirname(__file__)

PackageInstaller.try_install('rxvt-unicode-pixbuf')
PackageInstaller.try_install('xorg-fonts-misc')

FileInstaller.create_symlink(os.path.join(dir, 'rxvt-unicode'), '~/.Xresources.d/rxvt-unicode')
run_verbose(['xrdb', '-merge', os.path.expanduser('~/.Xresources.d/rxvt-unicode')])
