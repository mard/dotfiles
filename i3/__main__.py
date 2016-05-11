#!/bin/python
import os
import socket
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('i3-wm')
PackageInstaller.try_install('i3lock')
PackageInstaller.try_install('i3status')
PackageInstaller.try_install('feh')

sources = [os.path.join(dir, 'i3-config')]
if socket.gethostname() == 'sunjammer':
  FileInstaller.create_symlink(os.path.join(dir, 'a73', 'wrapper.py'), '~/.config/i3status/wrapper.py')
  sources.append(os.path.join(dir, 'a73/i3-config'))
else:
  sources.append(os.path.join(dir, 'pc/i3-config'))

FileInstaller.merge_files(sources, '~/.config/i3/config', '#')
FileInstaller.create_symlink(os.path.join(dir, 'i3status-config'), '~/.config/i3status/config')