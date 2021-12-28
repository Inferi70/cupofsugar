from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("sensei penguin, testing git.")
