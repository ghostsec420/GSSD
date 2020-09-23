#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.parse, urllib.error
import time
import os

def check(file_name, string):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string in line:
                return True

    return False
def check2(file_name, string):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string in line:
                return True

    return False
def check3(file_name, word_list_file):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            with open(word_list_file, 'r') as read_obj2:
              for line2 in read_obj2:
                if (line2 in line):
                  return True

    return False
print("GHOSTSEC - GSSD (Scam Detection Tool)")
site = input(' Enter site (make sure it is the exact url):')
showHTML = input('Show HTML? (True/False):')
true = True
print('Scanning ' + site + '...')
time.sleep(1)
html = urllib.request.urlopen(site).read()
html = str(html)
with open('url.txt', 'w+') as f:
    f.write(html)
if showHTML == True:
  print(html)
  os.system('clear')
  time.sleep(2)
isScam = False

"""" old code /ignore
 wordlist = open('wordlist.txt')
 all_the_lines = wordlist.readlines()
 opts = []
 for opts in opts:
  if check('url.txt', opts):
    print("Keyword found: " + opts)
    isScam = True
    break
"""

isScam = check3("url.txt","wordlist.txt")
  
if isScam == True:
    print(site + " is probably a scam")
else:
	print(site + " is most likely not a scam")


