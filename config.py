import configparser
import json

settings = configparser.ConfigParser()
settings.read("./data/settings.ini")

SETTINGS = {}
for key in settings:
    SETTINGS[key] = dict(settings[key])


secret = configparser.ConfigParser()
secret.read("./data/.secret/secret.ini")

SECRET = {}
for key in secret:
    SECRET[key] = dict(secret[key])

vk_data = SECRET.get('vk_data')


# Constants and Types

SLEEP_TIME = 30
DB_NAME = "cards_data.json"
BALANCE_UPDATE = "bl"


if __name__ == '__main__':
    print(SETTINGS)
    print(SECRET)
