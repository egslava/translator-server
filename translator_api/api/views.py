from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from translate import Translator

def index(request, source, target, text):
    trans = Translator(to_lang=target, from_lang=source)
    translation = trans.translate(text)
    # return HttpResponse(translation)

    return HttpResponse("""{ "data": { "translations": [ { "translatedText": "%s" } ] } }""" % translation)

# def index(request, text, source, target):
#     return HttpResponse("Hello, world. You're at the polls index.")