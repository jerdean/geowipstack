#! /usr/bin/python3

import re
import urllib.request
import json


pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

token = ("ADD YOUR API KEY HERE")

def getinfo(ip):
	#print ("received ip " + ip)
	
	match = re.match(pat, ip)
	if (match):
		api = 'http://api.ipstack.com/' + ip + '?access_key=' + token + '&format=1&fields=country_name,region_name,city,zip'
		location = urllib.request.urlopen(api).read()
		location = location.decode()
		location = json.loads(location)
		
		if location is None:
			return("Location Lookup Failed")
		else:
			return(location)

	else: 
		return('')

#read in file name
filename = input("Please enter file name: ")
first_line=next(open(filename))



#Lets get some informaiton about the fields in this file
fl = first_line.split(",")
place = 0
for i in fl:
	location = str(place)
	print (i + ' : ' + location)
	place = place + 1

print ("we will automatically print first name field [0] and last name field [1]\n")
print ("What are the IP address fields we should look up?\n")
print ("You only get 2...")
print ("enter as a comma separated list.\n")
print ("Example if columns 5 and 7 contain ips we want to look up\n")
ip_columns = input("enter 5,7 and press return:\n")
cols=ip_columns.split(",")
print ("let's double check...\n")
print ("checking these fields for IP info\n")
print (fl[int(cols[0])] + " and " + fl[int(cols[1])] )
keepgoing = input("Look good?  Type 'N' to stop or enter to continue.. ")
if keepgoing in ['n', 'N']:
	print ("Cool... try again")
	quit()

firstip = int(cols[0])
secip = int (cols[1])


f = open(filename, "r")
out = open("outfile.csv","w")
for line in f:
	x = line.split(",")
	if x[firstip] == '':
		continue
	data1 = getinfo(x[firstip])
	#print (data1)
	
	clickmatch = re.match(pat, x[secip])
	if (clickmatch):
		data2 = getinfo(x[secip])
		#print (data2)
	else:
		data2=''
	print (x[0] + ',' + x[1] + ',' + str(x[firstip]) + "," + str(data1) + "," + str(x[secip]) + "," + str(data2))
	out.write(x[0] + ',' + x[1] + ',' + str(x[firstip]) + "," + str(data1) + "," + str(x[secip]) + "," + str(data2) + "\n")
	




