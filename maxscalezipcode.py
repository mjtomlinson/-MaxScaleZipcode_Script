## Matt Tomlinson, mjtomlinson@student.rtc.org, 03/15/2022, winter quarter CNE 370-L713, 
##
## Talks to a Maxscale instance to query two separate data bases of zip codes for:
##
## The last 10 rows of database zipcodes_one
## The first 10 rows of database zipcodes_two
## The largest zipcode in database zipcodes_one
## The smallest zipcode in database zipcodes_two


import pymysql

db = pymysql.connect(host="172.18.158.93", port=8080, user = "maxuser, passwd = "maxpwd"
cursor = db.cursor()

print ('The last 10 rows of zipcodes_one are:')
cursor.execute("SELECT * FROM zipcodes_one.zipcondes_one LIMIT 9990.10;"
results = cursor.fetchall()
for result in results:
	print (result)

print ('The first 10 rows of zipcodes_two are:')
cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two LIMIT 10")
results = cursor.fetchall()
for result in results:
	print (result)

print ('The largest zipcode number in zipcodes_one is:')
cursor = db.cursor()
cursor.execute ("Select Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;"
results = cursor.fetchall()
for result in results:
	print (result)

print ('The smallest zipcode number in zipcodes_two is:')
cursor = db.cursor()
cursor.execute ("SELECT Zipcode FROM zipcodes_two.zipcodes_two ORDER BY Zipcode ASC LIMIT 1")
results = cursor.fetchall()
for result in results:
	print (result)
