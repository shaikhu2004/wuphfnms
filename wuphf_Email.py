import os
import smtplib

def wuphf_email(msg):
    Email_address = os.environ.get("wuphfmail_address")
    Email_password = os.environ.get("wuphfmail_pw")
    contacts = ["shaikhahmedkhan@hotmail.com", "shaikhahmedkhan2004@gmail.com"]

    message = 'Subject: {}\n\n{}'.format("IMPORTANT", msg)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(Email_address, Email_password)
    server.sendmail(Email_address, contacts, message)

    server.quit()
    print("Mail(s) were sent.")

wuphf_email("hello")



