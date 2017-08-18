#!/bin/python
import os
from libinstall import FileInstaller
dir = os.path.dirname(__file__)

FileInstaller.create_symlink(os.path.join(dir, 'minttyrc'), '~/.minttyrc')
