from django.shortcuts import redirect, get_object_or_404
from .models import Link


def show_url(request, code):
    link = Link.objects.get(code=code)
    return redirect(link.url)
