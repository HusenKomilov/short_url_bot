from django.db import models
from short_url import utils

SITE_URL = "https://www.newsite.uz/"


class Link(models.Model):
    url = models.CharField(max_length=400)
    code = models.CharField(max_length=6, unique=True, default=utils.generate_url_code)

    @property
    def short_ulr(self):
        return SITE_URL + self.code

    def __str__(self):
        return self.code
