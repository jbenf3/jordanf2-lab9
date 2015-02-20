#!/usr/bin/python2.7

# Init script from Lab #5

import sys
import os
import subprocess as sp
import re

def shell(cmd):
	return sp.check_output(cmd, shell=True)

user = shell('whoami').strip()
SUBMISSIONS = "/afs/ir.stanford.edu/class/physics91si/submissions/"
lab4dir = os.path.join(SUBMISSIONS, user, 'lab4')
target = 'language.py'

# Find language.py and check commit status
startdir = shell("pwd")
try:
	os.chdir(lab4dir)

	# hg update to show files, if necessary
	if not target in os.listdir('.'):
		ans = raw_input("%s not found in %s. Try hg update? \nWarning: this will overwrite current directory contents. [y/n] " % (target, lab4dir))
		if 'y' in ans:
			shell("hg update tip")
	if not target in os.listdir('.'):
		raise IOError
except:
	print "Error: unable to find %s" % os.path.join(lab4dir, target)
	exit()

os.chdir(startdir.strip())

# Copy over and commit
try:
	files = os.listdir('.')
	if target in files:
		ans = raw_input("%s exists. Overwrite? [y/n] " % target)
		if 'n' in ans: exit()
	shell("cp %s ." % os.path.join(lab4dir, target))
	shell("hg add %s" % target)
	print "%s copied from %s and added to repo" % (target, lab4dir)
except:
	print "Error: unable to copy %s" % target
	exit()

try:
	ans = raw_input("Commit to current repo? [y/n] ")
	if 'y' in ans:
		shell("hg commit -m \"auto-commit of %s\" %s" % (target, target))
except:
	print "Error: unable to commit %s" % target
	exit()

