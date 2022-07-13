from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello from index of app1")
    return render(request, 'app1/index.html')

def addnew(request):
    # display new form
    return render(request, 'app1/addnew.html')

def savenew(request):
    # receive data from webform and save on database table
    # receive data from webform
    pid=request.POST['txt1']
    fullname=request.POST['txt2']
    contactaddress=request.POST['txt3']
    print(pid, fullname, contactaddress)
    # save on database
    # -----
    return HttpResponse("Save record")
