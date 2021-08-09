import os
import tweepy
import smtplib
import requests
import pywhatkit
from datetime import datetime
from PIL import ImageFont, ImageDraw, Image
from instabot import Bot


message_to_be_spread = ("in harmony")
mailcontacts = ["MAIL_ID1", "MAIL_ID2"]
whatsappnumber = '+971phoneno'
instagram_postcaption = "yes"
#SENDING EMAILS

Email_address = os.environ.get("wuphfmail_address")
Email_password = os.environ.get("wuphfmail_pw")


message = 'Subject: {}\n\n{}'.format("IMPORTANT MAIL", message_to_be_spread)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(Email_address, Email_password)
server.sendmail(Email_address, mailcontacts, message)

server.quit()
print("Mail(s) were sent.")

#POSTING ON TWITTER

apikey = os.environ.get("twitter_apikey")
apisecret = os.environ.get("twitter_apisecret")
accesstoken = os.environ.get("twitter_accesstoken")
accesssecret = os.environ.get("twitter_accesssecret")

def OAuth():
    try:
        auth = tweepy.OAuthHandler(apikey, apisecret)
        auth.set_access_token(accesstoken, accesssecret)
        return auth
    except Exception as e:
        return None

oath = OAuth()
api = tweepy.API(oath)

api.update_status(message_to_be_spread)
print ("Tweeted.")

#POSTING TO FACEBOOK

page_id = os.environ.get("facebook_pageid")
access_token = os.environ.get("facebook_accesstoken")

post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)
payload={
    'message': message_to_be_spread,
    "access_token":access_token
}

r = requests.post(post_url,data=payload)
print(r.text)
print("Posted to Facebook.")

#POSTING TO INSTAGRAM
image = Image.new ('RGB', (900,900), 'white')
str1=message_to_be_spread

font = ImageFont.truetype("arial.ttf",75)
w,h = font.getsize(str1)

draw = ImageDraw.Draw(image)
draw.text(((900-w)/2,(900-h)/2),str1,font=font,fill="black")
image.save('instapics/{}.jpg'.format(str1))

instausername = os.environ.get ('instagram_username')
instapw = os.environ.get ('instagram_password')

bot = Bot()

bot.login(username=instausername, password = instapw)

bot.upload_photo('instapics/{}.jpg'.format(str1), caption=instagram_postcaption)


#SEND WHATSAPP MESSAGES

now = datetime.now()

currenthr = now.strftime("%H")
currentmin = now.strftime("%M")
sendinghr = int(currenthr)
sendingmin = int(currentmin) + 3

if sendingmin > 55:
    sendinghr=sendinghr+1
    sendingmin=3
else:
    None

if 1 <= sendingmin <= 9:
    sendingmin = (f"{sendingmin:02}")
else:
    None

print (sendinghr, sendingmin)

pywhatkit.sendwhatmsg(whatsappnumber, message_to_be_spread, sendinghr, sendingmin)
print ("WhatsApp message Sent.")
