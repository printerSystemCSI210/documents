# Michael Borowsky
# 11/7/13
# Proof of Concept- get a printer's html page and parse it for information

import urllib.request
import re

# The url of the device status page for the printer
url = 'https://192.168.130.238/hp/device/this.LCDispatcher?nav=hp.DeviceStatus'

# Read get the html as a string
html = urllib.request.urlopen(url).read().decode("utf8")

# Parse the string
for c in range( 0, len(html)-7 ):
	# Find "Tray 2"
	if html[c:c+6]=="Tray 2":
		# Find the status of Tray 2
		for x in range(c,c+200):
			if html[x:x+2]=="OK":
				print("Tray 2: OK")
			elif html[x:x+5]=="Empty":	# if the first letter is an "E", the status is "Empty"
				print("Tray 2: Empty")
