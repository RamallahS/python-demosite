from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    response = "You're looking at the results of question"
    return HttpResponse(response)
