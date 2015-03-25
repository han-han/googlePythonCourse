#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_dir(dir):
  filenames = os.listdir(dir)
  spnamelist = []
  for filename in filenames:
      spname = re.search(r'\w+_\w+_[\w._]+', filename)
      if spname: 
         spnamelist.append(os.path.abspath(os.path.join(dir, spname.group())))
  return spnamelist
  
def copy_to(paths, dir):
  for file in paths:
    shutil.copy(file, dir)

def zip_to(paths, zippath):
  cmd = 'zip -j' + ' ' + zippath + ' ' + ' '.join(paths)   
  print "Command to run: ", cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
    
  for dirname in args:
      spnames = get_special_dir(dirname)
      if tozip == '' and todir == '': 
        print spnames
      elif todir <> '':
        copy_to(spnames, todir) 
      elif tozip <> '':
        zip_to(spnames, tozip)  

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
