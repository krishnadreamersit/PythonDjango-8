from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from epanel.models import UserInfo

def index(request):
    # get all users
    users = UserInfo.objects.all()
    # print(users)
    # Task
        # alert user on insert
        # display records with multi-page
    return render(request, 'epanel/index.html', {'users':users})


def new(request):
    if request.method =='GET':
        # get method - default
        return render(request, 'epanel/new.html')
    elif request.method == 'POST':
        # post method - specified
        # read values from web form and save in database
        try:
            username = request.POST['txtUser']
            password = request.POST['txtPassword']
            fullname = request.POST['txtFullName']
            email = request.POST['txtEmail']
            # print(username, password, fullname, email)
            newUser = UserInfo(username=username, password=password, fullname=fullname, email=email)
            newUser.save()
            # return HttpResponse("Save record successfully");
            return redirect('/')
        except:
            return HttpResponse("Error to save record");

def edit(request):
    if request.method == 'GET':
        return render(request, 'epanel/edit.html')
    elif request.method=='POST':
        return redirect('/')

def delete(request):
    if request.method=='GET':
        return render(request, 'epanel/delete.html')
    elif request.method == 'POST':
        return redirect('/')