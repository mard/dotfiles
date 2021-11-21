#!/bin/python
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)

PackageInstaller.try_install('yt-dlp', 'pip')

FileInstaller.create_symlink(os.path.join(dir, 'config'), '~/.config/yt-dlp/config')
