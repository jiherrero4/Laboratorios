# coding=utf-8
import json
import requests

myToken="YzRjYTFiZDktNDcwOS00N2I2LTg5NDYtZjA4YTYwZGQzN2MyMjFmNWI2YzEtYWMx"
myRoom="Y2lzY29zcGFyazovL3VzL1JPT00vZjhhMWI4NjAtNTBmMC0xMWU2LTk1MGYtMjljZDY4MTAwZDI5"
myToken="Bearer "+myToken

def get_memberships(mytoken,myroom):
	# The header is send to authenticate 
	header = {'Authorization':mytoken, 'content-type':'application/json'}
	# NEW: Besides the header for authentication we want to specify the
	# room, that's what we send in the payload.
	payload = {'roomId':myroom}
	# Send GET request with above header+payload. Put result in 'result'
	result = requests.get(url='https://api.ciscospark.com/v1/memberships',
                                headers=header,params=payload)
	# Encode 'result' as JSON
	JSONresponse = result.json()
	# Create an Array for all rooms: ('name1','name2','name3')
	memberlist_array = []
	# For each item in the JSON data
	for EachMember in JSONresponse['items']:
		# add the 'title' to the roomlist_array
		memberlist_array.append(EachMember.get('personDisplayName'))
	# Return the list of members
	return memberlist_array


# Execute get_memberships and put result in 'SparkResult'
SparkResult = get_memberships(myToken, myRoom)
# Loop through the 'SparkResult' array
for member in SparkResult:
	# print member name
	print ("> Member:", member)
# Print the number of rooms (length of SparkResult array)
print ("----- TOTAL Room Count:", len(SparkResult))
