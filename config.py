import os
from functools import lru_cache

class TWConfig(object):
    consumer_key: str
    access_token: str
    consumer_secret: str
    access_token_secret: str

    def validate(self):
        try:
            if self.consumer_key is None:
                raise ValueError("TW_CONSUMER_KEY is not set")

            if self.access_token is None:
                raise ValueError("TW_ACCESS_TOKEN is not set")

            if self.consumer_secret is None:
                raise ValueError("TW_CONSUMER_SECRET is not set")

            if self.access_token_secret is None:
                raise ValueError("TW_ACCESS_TOKEN_SECRET is not set")
        except AttributeError:
            raise RuntimeError("One or more keys are not set for TWConfig")

@lru_cache(maxsize=16)
def get_config():
    conf = TWConfig()
    
    conf.consumer_key = os.environ.get("TW_CONSUMER_KEY", None)
    conf.consumer_secret = os.environ.get("TW_CONSUMER_SECRET", None)
    conf.access_token = os.environ.get("TW_ACCESS_TOKEN", None)
    conf.access_token_secret = os.environ.get("TW_ACCESS_TOKEN_SECRET", None)

    conf.validate()

    return conf