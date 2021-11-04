import os
import tweepy
import smtplib
import requests
import pywhatkit
from datetime import datetime
from instabot import Bot
from PIL import ImageFont, ImageDraw, Image
from twilio.rest import Client

message_to_be_spread = input("Enter Message to be Posted: ")


contacts = ["shaikhahmedkhan@hotmail.com", "shaikhahmedkhan2004@gmail.com"]
whatsappnumber = '+971554657145'
phonenumberforcall = '+971585310804'


#SENDING EMAILS

def wuphf_email():
    Email_address = os.environ.get("wuphfmail_address")
    Email_password = os.environ.get("wuphfmail_pw")

    message = 'Subject: {}\n\n{}'.format("IMPORTANT", message_to_be_spread)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(Email_address, Email_password)
    server.sendmail(Email_address, contacts, message)

    server.quit()
    print("Mail(s) were sent.")


#POSTING ON TWITTER

def wuphf_twitter():
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
    print("Tweeted.")


#POSTING TO FACEBOOK

def wuphf_facebook():
    page_id = os.environ.get("facebook_pageid")
    access_token = os.environ.get("facebook_accesstoken")
    msg = message_to_be_spread

    post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)
    payload = {
        'message': msg,
        "access_token": access_token
    }

    r = requests.post(post_url, data=payload)

    print("Posted to Facebook.")


#POSTING TO INSTAGRAM

def wuphf_instagram():
    image = Image.new('RGB', (900, 900), 'white')
    str1 = message_to_be_spread

    font = ImageFont.truetype("arial.ttf", 75)
    w, h = font.getsize(str1)

    draw = ImageDraw.Draw(image)
    draw.text(((900 - w) / 2, (900 - h) / 2), str1, font=font, fill="black")
    image.save('instapics/{}.jpg'.format(str1))

    instausername = os.environ.get('instagram_username')
    instapw = os.environ.get('instagram_password')

    bot = Bot()

    bot.login(username=instausername, password=instapw)

    bot.upload_photo('instapics/{}.jpg'.format(str1), caption="Wuphf NMS")

    print ("Posted to Instagram.")


#SEND WHATSAPP MESSAGES

def wuphf_whatsapp():
    now = datetime.now()

    currenthr = now.strftime("%H")
    currentmin = now.strftime("%M")
    sendinghr = int(currenthr)
    sendingmin = int(currentmin) + 2

    if sendingmin > 55:
        sendinghr = sendinghr + 1
        sendingmin = 2
    else:
         None

    if 1 <= sendingmin <= 9:
        sendingmin = (f"{sendingmin:02}")
    else:
        None

    pywhatkit.sendwhatmsg(whatsappnumber, message_to_be_spread, sendinghr, sendingmin)

#SEND A CALL

def wuphf_phonecall():
    msg = message_to_be_spread

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml='<Response><Say>This is an urgent message from Shaikh. {}</Say></Response>'.format(msg),
        to=phonenumberforcall,
        from_='+19032284789'
    )

    print("Call was sent.")






#!!!SENDING MESSAGES!!!

ifsend_mail= input("Send Mails? : ")
ifpost_facebook= input("Post on Facebook? : ")
ifpost_twitter= input("Tweet? : ")
ifsend_call= input ("Send a Call with a Voice Message?: ")
ifpost_instagram= input("Post on Instagram? : ")
ifpost_whatsapp= input("Send WhatsApp Message? : ")

if ifsend_mail == "y":
    wuphf_email()
else:
    None

if ifpost_facebook == "y":
    wuphf_facebook()
else:
    None

if ifpost_twitter == "y":
    wuphf_twitter()
else:
    None

if ifsend_call == "y":
    wuphf_phonecall()
else:
    None

if ifpost_instagram == "y":
    wuphf_instagram()
else:
    None

if ifpost_whatsapp == "y":
    wuphf_whatsapp()
else:
    None
