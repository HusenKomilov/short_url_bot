import random
import string
from short_url import models


def generate_url_code():
    length = 6

    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=length))
        if not models.Link.objects.filter(code=code).exists():
            break
    return code
