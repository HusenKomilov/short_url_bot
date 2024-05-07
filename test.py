URL = "https://github.com/apache/superset/blob/10c78960a7c5e5628aaceb584c206a81f7fd12c8/superset/connectors/sqla/models.py#L302"

import string
import random

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))  # 6-character short URL
    return short_url

url = {}

def shorts(sht_url):
    short = string.printable

shorts(URL)