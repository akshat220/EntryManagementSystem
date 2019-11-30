from datetime import datetime
import mysql.connector
import config
import smtplib
from twilio.rest import Client

active_visitors = {}

#checking if the number is of 10 digit and all numbers are intergers in it
def check_phone(number):
	if len(number) != 10 :
		return False
	try :
		val =  int(number)
	except:
		return False
	return True

#connecting to database innov
def giveDb():
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="root"	,
		database="innov"			#your mysql Password
	)
	return mydb


def add_to_db(email,name,phone,address,checkin,host_name,host_email,host_phone):
	mydb = giveDb()
	mycursor = mydb.cursor()
	query = "Insert Into visitor (email,name,contact)  values (%s,%s,%s)"
	values = (email,name,phone)
	mycursor.execute(query,values)
	query_host = "Insert into host (email, name, contact) values (%s, %s, %s)"
	values_host = (host_email,host_name,host_phone)
	mycursor.execute(query_host,values_host)
	queryA = "Insert into entryManagement (host_email, guest_email, checkin, checkout) values(%s,%s,%s,%s)"
	valuesA = (host_email,email,checkin,None)
	mycursor.execute(queryA,valuesA)
	mydb.commit()

#sending mail using smtp
def send_mail(message, subject, receiver):
	try:
		print("sending email\n")
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login(config.email, config.password)
		message = "Subject : {}  \n\n  {}".format(subject,message)
		s.sendmail(config.email, receiver, message)
		print("email sent to" + receiver)
		s.quit()

	except:
		print("Sorry The email can't be send")	

#sending sms using twilio
def send_sms(message, receiver):
	try :
		account_sid = 'ACc2bd47eaaeefdd4152ba8ae2ba25bd15'
		auth_token = '17ecd90a0349215541904926e1db2941'
		client = Client(account_sid, auth_token)

		message = client.messages \
	    	.create(
	        	 body= message,
	         	from_='+12056193680',
	         	to= receiver
	     	)
		print("message sent to host")

	except:
		print("Sorry The message can't be send")

#function for checkin
def add_visitor():
	print("Enter Your Details")
	visitor_email = input("Enter email: ")
	name = input ("Enter name: ")
	phone = input("Enter 10 digit phone number: ")
	if check_phone(phone) == False :
		print("Enter a valid phone number: ")
		phone =  input("Enter 10 digit phone number: ")
	address = input("Enter address: ") 
	checkin_time = datetime.now()	
	dt_string = checkin_time.strftime("%Y-%m-%d %H:%M:%S")
	active_visitors[visitor_email] = [name,phone,address,dt_string]

	print("Enter Host Details")
	host_name = input("Enter host_name: ")
	host_email = input("Enter host_email: ")
	host_phone = input("Enter host_phone_number: ")

	message = "Visitor Details\n"
	message = message + "Name: " + name + "\n"
	message = message + "Email: " + visitor_email + "\n"
	message = message + "Phone: " + phone + "\n"
	message = message + "Checkin date and time: " + dt_string 

	send_mail(message, "You Have a Visitor", host_email)
	add_to_db(visitor_email,name,phone,address,dt_string, host_name, host_email, host_phone)
	host_phone = "+91"+host_phone
	send_sms(message, host_phone)


def get_visitor(email, checkout_time):
	send_data = []
	mydb = giveDb()
	mycursor = mydb.cursor()

	qx = "update entryManagement set checkout = %s where guest_email = %s;"
	z = (checkout_time, email)
	mycursor.execute(qx,z)
	mydb.commit()

	query = "Select * from entryManagement where guest_email = %s;"
	mycursor.execute(query,(email,))
	record = mycursor.fetchone()
	
	queryB = "Select * from visitor where email = %s"
	mycursor.execute(queryB,(email,))
	record2 = mycursor.fetchone()
	
	queryC = "Select * from host where email=%s"
	mycursor.execute(queryC,(record[0],))
	record3 = mycursor.fetchone()

	message = "Details\n"
	message = message + "Name: " + record2[1] + "\n"
	message = message + "Phone: "  + record2[2] + "\n"
	message = message + "Checkin: " + str(record[2]) + "\n"
	message = message + "Checkout: "  + str(record[3]) + "\n"
	message = message + "host: " + record3[1] + "\n"
	send_mail(message, "Thankyou for Comimg", email)

def check_out():
	visitor = input("Enter Visitor Email: ")
	checkout_time = datetime.now()
	dt_string = checkout_time.strftime("%Y-%m-%d %H:%M:%S")
	get_visitor(visitor, dt_string)
	




print('1. checkin visitor')
print('2. checkout visitor')

choice = int(input("enter choice: "))

if choice == 1 :
	add_visitor()
else :
	check_out()




