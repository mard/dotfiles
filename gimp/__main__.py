#!/usr/bin/env python3
import os
from libinstall import FileInstaller, PackageInstaller
dir = os.path.dirname(__file__)
ver = '2.x'

FileInstaller.create_symlink(os.path.join(dir, ver), f"~/.config/GIMP/{ver}-dotfiles")
print(f"cp -rL ~/.config/GIMP/{ver}-dotfiles ~/.config/GIMP/$(gimp --version | awk -v FS=\"(version |.[0-9]+$)\" '{{print $2}}')")
