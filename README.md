dotfiles
--------

This repository contains configuration files and scripts tailored to my needs
or preferences. Some of these might prove useful to other people.

### Installation

The repository is divided into modules. All of modules can be installed with
Python 3 like this:

    python -m X

for example,

    python -m i3
    python -m vim

will install i3 and vim configuration.

The installation scripts also try to install relevant packages using various
package managers, e.g. vim will try downloading only vim, while i3 will download
i3-wm, i3status and other dependencies required for full i3 setup.

### Platforms

Some modules will work only on GNU/Linux, but essential ones such as vim will
also work on Cygwin.