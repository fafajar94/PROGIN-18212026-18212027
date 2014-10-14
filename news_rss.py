#!/usr/bin/python

from xml.dom import minidom
#import urllib
#url='http://www.antaranews.com/rss/nas.xml'
#xmldoc = minidom.parse(urllib.urlopen(url))
xmldoc = minidom.parse('detik.xml')
itemlist = xmldoc.getElementsByTagName('item')
print len(itemlist)
for s in itemlist:
	print s.childNodes[1].nodeName + " = " + s.childNodes[1].childNodes[0].nodeValue
#	print s.childNodes[3].nodeName + " = " + s.childNodes[3].childNodes[0].nodeValue
#	print s.childNodes[5].nodeName + " = " + s.childNodes[5].childNodes[0].nodeValue
#	print s.childNodes[7].nodeName + " = " + s.childNodes[7].childNodes[0].nodeValue
#	print s.childNodes[9].nodeName + " = " + s.childNodes[9].childNodes[0].nodeValue
#	print s.childNodes[11].nodeName + " = " + s.childNodes[11].childNodes[0].nodeValue
	print
