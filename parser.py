#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree
import sys

tree = etree.parse(sys.argv[1])
root = tree.getroot()
for artist in root.findall("./artists/artist/name"):
	print artist.text.encode('utf-8')
