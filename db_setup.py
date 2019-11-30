import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="root"				#your mysql Password
	)


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE innov")
mycursor.execute("use innov")

mycursor.execute("CREATE TABLE visitor (email VARCHAR(255) PRIMARY KEY,name VARCHAR(255),contact VARCHAR(13))")
mycursor.execute("CREATE TABLE host (email VARCHAR(255) PRIMARY KEY,name VARCHAR(255),contact VARCHAR(13))")
mycursor.execute("CREATE TABLE entryManagement (host_email VARCHAR(255), guest_email VARCHAR(255), checkin DATETIME, checkout DATETIME) ")

