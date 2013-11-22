#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree
import sys

user = (sys.argv[1], sys.argv[2])
tree = (etree.parse(user[0]), etree.parse(user[1]))
root = (tree[0].getroot(), tree[1].getroot())
artists = (root[0].findall("./artists/artist/name"), root[1].findall("./artists/artist/name"))

print "<html>"
print "<body>"

print "<h1>What awesome for " + user[0] + " in " + user[1] + "</h1>"
for artist1 in artists[0]:
	for artist2 in artists[1]:
		if artist1.text == artist2.text:
			print "<p>" + artist2.text.encode('utf-8') + "</p>"

print "<h1>What awesome for " + user[1] + " in " + user[0] + "</h1>"
for artist2 in artists[1]:
	for artist1 in artists[0]:
		if artist1.text == artist2.text:
			print "<p>" + artist2.text.encode('utf-8') + "</p>"

print "</body>"
print "</html>"
