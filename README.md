# Innovaccer SDE Summer Intern Assignment

In the given project I have made an entry management software.
The main aim of the project is to store all of the information with time stamp of each entry.

## Project Description

This application takes the details from visitor at the time of check-in and trigger an email and a message to the host according to the visitor details. At the time of check-out it takes visitor email as an input and then trigger an email to the visitor. 

## Tech Stack

1. Python
2. MySQL
3. smtplib: to send emails.
4. twilio: to send messages.

## Database is designed as follows:

To make my task easier I created three tables under the database 'innov'.
``` 
   innov
     |__ visitor
            |__ email
            |__ name
            |__ contact
            
     |__ host
            |__email
            |__name
            |__contact
            
     |__entryManagement
            |__host_email
            |__guest_email
            |__checkin
            |__checkout
  ```


## Basic Workflow

Run main.py file, you will get two choices as you can see in the screenshot.
If you select check-in it will ask for visitor and host details and then send an email and a message to the host.

![](https://github.com/akshat220/Innovaccer/blob/master/checkint1.png) 
![](https://github.com/akshat220/Innovaccer/blob/master/checkint2.png)


If you select check-out it will ask for visitor's email and then send an email to the visitor.

![](https://github.com/akshat220/Innovaccer/blob/master/checkout_terminal.png)


Entries will get stored in the database tables.

![](https://github.com/akshat220/Innovaccer/blob/master/database.png)


Some screenshot of emails and messages received by host at the time of check-in.

Email | Message
------------ | -------------
<img src="https://github.com/akshat220/Innovaccer/blob/master/sent_to_host.png" width="720" height="740"> | ![](https://github.com/akshat220/Innovaccer/blob/master/msg_sent_to_host.jpg)



Some screenshot of emails received by visitor at the time of check-out.

ScreenShot1 | ScreenShot2
------------ | -------------
![](https://github.com/akshat220/Innovaccer/blob/master/byvisitor1.jpg) | ![](https://github.com/akshat220/Innovaccer/blob/master/byvisitor2.jpg)


## Setup

### Step-1

Install the following libraries in python:
1. mysql.connector
2. twilio.rest

Using the command:

1. ```pip install mysql-connector-python```
2. ```pip install twilio```

### Step-2

1. Write the MySQL username and password in ```config3.py``` for connecting to MySQL server.

### Step-3

1. Write the email id and password in ```config.py``` that you want to use for sending emails.
2. Go to https://myaccount.google.com/security?pli=1#connectedapps and then click ```Allow less secure app``` to YES

### Step-4

1. Write the twilio sid, token and number in ```config1.py``` that you want to use for sending messages.

### Step-5

1. Run ```db_setup.py``` using the command
   ```python db_setup.py```
   to create database in your system. (Note: This file should be run only once in a system)
2. Now run ```main.py``` using the command
   ```python main.py```
   and select checkin or checkout as required.


