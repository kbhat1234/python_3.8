#!/usr/bin/python3
import smtplib

sender_mail = 'kbhat.anurag@gmai.com'
receivers_mail = ['karthikkbhat@yahoo.co.in']
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
""" % (sender_mail, receivers_mail)
try:
    password = input("enter the password")
    smtpObj = smtplib.SMTP('gmail.com', 587)
    smtpobj.login(sender_mail, password)
    smtpObj.sendmail(sender_mail, receivers_mail, message)
    print("Successfully sent email")
except Exception:
    print("Error: unable to send email")
