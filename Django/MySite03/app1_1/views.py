from django.shortcuts import render

from django.http import HttpResponse # output library # 1

# Create your views here.

# view function # 2

def index(request):
    return render(request, 'app1_1/index.html')