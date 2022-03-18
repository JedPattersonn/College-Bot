import requests
import csv
from logger import Logger
import smtplib
import time


class CollegeEmailer:
    
    #fill these details in first
    email = "" #your gmail address
    password = "" #your gmail password
    name = "" #your name
    schoolName = "" #your current high school
    state = "" #your state
    address = "" #your address
    

    with open('collegeemails.csv', newline='') as csvfile:
        emails = list(csv.reader(csvfile))
        
    for collegeEmail, collegeName in emails:
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
    
            # start TLS for security
            s.starttls()
            
            # Authentication
            s.login(email, password)
            
            # message to be sent
            subject = f"Attending {collegeName} in the Fall"
            body = f"Hi there, my name is {name} and I am currently a senior at {schoolName} in {state}. I am planning on attending in the fall of 2022. I toured your campus and it just feels like the perfect fit for me. I'm sure you get a lot of these requests, but I was wondering if there is any chance I could receive a pennant, flag, shirt or really anything you guys are able to offer me! I would love to start representing my school pride as early as possible. If you guys are able to help me out, my address is {address} I am looking forward to being a student and getting my collegiate career started!" 
            message = f"Subject: {subject}\n{body}"
        
            
            # sending the mail
            s.sendmail(email, collegeEmail, message)
            
            # terminating the session
            s.quit()
        
            Logger.success(f"Successfully sent an email to {collegeName}")

            time.sleep(1.5)    
        except:
            Logger.error(f"Error sending an email to {collegeName}")
            time.sleep(1)
