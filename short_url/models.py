from django.db import models
from short_url import utils

SITE_URL = "http://127.0.0.1:8000/"


class Link(models.Model):
    url = models.CharField(max_length=400)
    code = models.CharField(max_length=6, unique=True, default=utils.generate_url_code)

    @property
    def short_url(self):
        return SITE_URL + self.code

    def __str__(self):
        return self.code
