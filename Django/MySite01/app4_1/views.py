from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "app4_2/Third.html")

def static_contents(request):
    return render(request, "app4_2/Fourth.html")