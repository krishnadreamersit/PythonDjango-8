from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'app2_1/index.html')


def getValues1(request):
    return HttpResponse("Welcome to getValues1")