from django.shortcuts import render
from django.http import HttpResponse
from pkg1 import person
from pkg1 import mydb

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

    p1 = person.Person(pid, fullname, contactaddress)
    mydb.insertRecord(p1)

    return HttpResponse("Save record")
