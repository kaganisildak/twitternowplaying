import tweepy

from config import get_config

def change_desc(desc):
    # Get keys, tokens and secrets from the envvars
    conf = get_config()

    # authorization of consumer key and consumer secret
    auth = tweepy.OAuthHandler(conf.consumer_key, conf.consumer_secret)

    # set access to user's access key and access secret
    auth.set_access_token(conf.access_token, conf.access_token_secret)

    # calling the api
    api = tweepy.API(auth)

    description = desc

    # updating the profile description
    api.update_profile(description=desc)
