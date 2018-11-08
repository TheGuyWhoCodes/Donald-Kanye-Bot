import tweepy
from time import sleep
from credentials import *
from sample import *
auth = tweepy.OAuthHandler("ts3mzJa09N8tkM1R6OzDhlQ5p", "g580zOKkwnILyANbdx7V8jV3j6MtJAuAfO6nqdm4Fa5pE522mW")
auth.set_access_token("1055101400294834176-VDnw6eOdiYaEdpDcqIfX5iugiJGbp7", "XQy5e80XnXgRf7C7rf7vuKCtNJgZAgRyw05WJtbMTqNYF")
api = tweepy.API(auth)
thistext = "A.I. says: " + main()
api.update_status(thistext)
print thistext
