import tweepy
import configparser
from pathlib import Path


def setup_twitter():
    config = configparser.ConfigParser()

    # Determine the path to the config.ini file which is one level up
    config_path = Path(__file__).parent.parent / "config.ini"

    config.read(config_path)

    api_key = config['Twitter']['API_KEY']
    api_secret_key = config['Twitter']['API_SECRET_KEY']
    access_token = config['Twitter']['ACCESS_TOKEN']
    access_token_secret = config['Twitter']['ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)


def tweet_to_isp(api, isp_handle, speed):
    tweet_content = f"Hey {isp_handle}, my internet speed is currently {speed} Mbps, which is below the expected threshold! #SlowInternet"
    api.update_status(status=tweet_content)
