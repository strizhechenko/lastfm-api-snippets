#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree
import sys

tree = etree.parse(sys.argv[1])
root = tree.getroot()
for artist in root.findall("./artists/artist/name"):
	print artist.text.encode('utf-8')
#for track in root.findall("./artist/"):
#	print track
#	artist = 0
#	name = 0
#	for node in track:
#		if node.tag == "key" and node.text == "Name":
#			name = 1
#		if node.tag == "string" and name == 1:
#			nametext = node.text
#			name = 0
#		if node.tag == "key" and node.text == "Artist":
#			artist = 1
#		if node.tag == "string" and artist == 1:
#			line = u'%s - %s' % (node.text, nametext)
#			print line.encode('utf-8')
#			artist = 0
#
