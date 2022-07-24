import django.http
from django.shortcuts import render
from epanel.models import UserInfo

def index(request):
    # get all users
    users = UserInfo.objects.all()
    print(users)
    return render(request, 'epanel/index.html', {'users':users})

def new(request):
    return render(request, 'epanel/new.html')