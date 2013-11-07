import urllib.request
import re

# The url of the device status page for the printer
url = 'https://192.168.130.238/hp/device/this.LCDispatcher?nav=hp.DeviceStatus'

# Read get the html as a string
html = urllib.request.urlopen(url).read().decode("utf8")

# Parse the string (this is a pretty poor way to parse it)
for c in range(0, len(html)):
	# Find "Tray 2"
	if html[c]=='T' and html[c+1]=='r' and html[c+2]=='a' and html[c+3]=='y' and html[c+5]=='2':
		# html[c+163] will be the first letter of the status of the printer 
		if html[c+163]=='O':	# if the first letter is an "O", the status is "OK"
			print("Tray 2: OK")
		elif html[c+163]=="E":	# if the first letter is an "E", the status is "Empty"
			print("Tray 2: Empty")

		break # Finished parsing, exit