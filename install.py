#!/usr/bin/env python

# Vectorguo <vectorguo@gmail.com>
#
# installer for my dotfiles
#
# usage:
#   ./install.py [subdir]
#       install the dot files into HOME dir, and do backup for each overwritten files/folders
#
#   ./install.py --no-backup
#       install the dot files into HOME dir, without backup for overwritten files/folders


import os
import sys

home = os.getenv("HOME")

if len(sys.argv) > 1:
    os.chdir(sys.argv[1])

if os.path.exists("install.py"):
    print "please specify a subdir, or run this script form a subdir!"
    exit(1)

def my_exec(cmd):
    print cmd
    os.system(cmd)

print "Installing from %s" % os.getcwd()

for e in os.listdir("."):
    if e.startswith("_"):
        f = "." + e[1:]
        if os.path.isdir(e):
            print "# dir: " + e
            if "--no-backup" not in sys.argv:
                my_exec('rm -rf "%s"' % os.path.join(home, f + ".backup"))
                my_exec('mv "%s" "%s"' % (os.path.join(home, f), os.path.join(home, f + ".backup")))
            else:
                my_exec('rm -rf "%s"' % os.path.join(home, f))
            my_exec('cp -r "%s" "%s"' % (e, os.path.join(home, f)))
        else:
            print "# file: " + e
            if "--no-backup" not in sys.argv:
                my_exec('rm -f "%s"' % os.path.join(home, f + ".backup"))
                my_exec('mv "%s" "%s"' % (os.path.join(home, f), os.path.join(home, f + ".backup")))
            else:
                my_exec('rm -f "%s"' % os.path.join(home, f))
            my_exec('cp "%s" "%s"' % (e, os.path.join(home, f)))

