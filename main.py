import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import *
from time import sleep

print('''
Welcome to the Email Checker 9000
This is an example of a part of the program that can be found during the registration of a site.
Entirely made with python by the Wati-Dev ''')

sleep(1)

print('''\nDo you want to try it ?
Yes / No''')
ans = input("")


def start():
    global code
    your = input("\nEnter your email (works only with Hotmail for the moment): ")
    passw = input("Enter the password of the email (this program doesn't register your password) : ")
    target = input("Enter a mail that will receive the verification code : ")
    print("Sending the email...")
    body = "YOUR CODE IS :    "
    code = ""
    for i in range(6):
        num = str(randint(0, 9))
        body += num
        code += num


    msg = MIMEMultipart()
    msg['From'] = str(your)
    msg['To'] = str(target)
    password = str(passw)
    msg['Subject'] = 'Verify Me'
    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP('smtp-mail.outlook.com: 25')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    verify()

def verify():
    a = input("\nYou will receive a email in about less than 1 min, please write the code here :")
    while a != code:
        print("Verification...")
        sleep(2)
        print("\n\nPassword not accepted, please retry : ")
        a = input("")
    print("Verification...")
    sleep(2)
    return print("\n\nPassword accepted, thank you for using the Email Checker 9000")

if ans in ["Yes", "yes", "Y", "y"]:
    sleep(2)
    start()
if ans in ["No", "no", "N", "n"]:
    print("Ok, ending the program...")
    pass
