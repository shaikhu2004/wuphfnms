from instabot import Bot
import os
from PIL import ImageFont, ImageDraw, Image

def wuphf_instagram(str1):
    image = Image.new('RGB', (900, 900), 'white')

    font = ImageFont.truetype("arial.ttf", 75)
    w, h = font.getsize(str1)

    draw = ImageDraw.Draw(image)
    draw.text(((900 - w) / 2, (900 - h) / 2), str1, font=font, fill="black")
    image.save('instapics/{}.jpg'.format(str1))

    instausername = os.environ.get('instagram_username')
    instapw = os.environ.get('instagram_password')

    bot = Bot()

    bot.login(username=instausername, password=instapw)

    bot.upload_photo('instapics/{}.jpg'.format(str1), caption="bruh indeed")

    Print("Posted to Instagram")




