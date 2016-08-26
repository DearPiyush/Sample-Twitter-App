import tweepy
consumer_key = ''
consumer_secret = ''
Access_Token = ''
Access_Secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(Access_Token, Access_Secret)
api = tweepy.API(auth)
api.update_status(status="Hello Twitter!!")

