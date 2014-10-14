from xml.dom import minidom
import urllib
import datetime
import time


xmldoc = minidom.parse('detik.xml')

item_values = xmldoc.getElementsByTagName('item')
item_values.sort(key=lambda x: time.strptime(x.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue, '%a, %d %b %Y %H:%M:%S %Z'), reverse=True) 

for s in item_values:
	pubDate = s.getElementsByTagName('pubDate')[0]
	pubTime = datetime.datetime.fromtimestamp(time.mktime(time.strptime(pubDate.childNodes[0].nodeValue, '%a, %d %b %Y %H:%M:%S %Z')))
	curTime = datetime.datetime.now()
	difTime = (curTime - pubTime)
	difTime = difTime.seconds + difTime.days*24*60*60
	if difTime <= 86400:
		print s.childNodes[1].nodeName + " = " + s.childNodes[1].childNodes[0].nodeValue
    		print s.childNodes[3].nodeName + " = " + s.childNodes[3].childNodes[0].nodeValue
		print s.childNodes[9].nodeName + " = " + s.childNodes[9].childNodes[0].nodeValuefro