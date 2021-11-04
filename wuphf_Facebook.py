import requests
import os

def wuphf_facebook(msg):
    page_id = os.environ.get("facebook_pageid")
    access_token = os.environ.get("facebook_accesstoken")

    post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)
    payload = {
        'message': msg,
        "access_token": access_token
    }

    r = requests.post(post_url, data=payload)

    return ("Posted to Facebook")

