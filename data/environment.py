import os
from dotenv import load_dotenv


class Environment:
    STAGE = 'stage'
    PROD = 'prod'

    URLS = {
        STAGE: 'https://www.saucedemo.com/1',
        PROD: 'https://www.saucedemo.com/'
    }

    def __init__(self):
        load_dotenv()
        try:
            self.env = os.getenv('ENV')
        except KeyError:
            self.env = self.PROD

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")
