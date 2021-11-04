import tweepy
import os

def wuphf_twitter(msg):
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

    api.update_status(msg)
    print("Tweeted.")

