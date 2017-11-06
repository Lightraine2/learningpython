#!/usr/bin/python

import re

def Main():
	line = "I think I understand regular expressions"

	matchResult = re.match(r'think', line, re.M|re.I)
	if matchResult:
		print "Match Found: " + matchResult.group()
	else:
		print "No match was found"

	searchResult = re.search(r'think', line, re.M|re.I)
	if searchResult:
		print "Search Found: " + searchResult.group()
	else:
		print "Nothing found in search"

if __name__ == '__main__':
	Main()
