from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from epanel.models import UserInfo
from django.forms.models import model_to_dict

def index(request):
    # get all users
    users = UserInfo.objects.all()
    # print(users)
    # Task
        # alert user on insert
        # display records with multi-page
    print("Index " + str(request.session['CurrentUser']))
    cUser = request.session['CurrentUser'];
    return render(request, 'epanel/index.html', {'users':users, 'cuser':cUser})


def login(request):
    if request.method=='GET':
        return render(request, 'epanel/login.html')
    elif request.method=='POST':
        # receive login info from login form
        username = request.POST['txtUser']
        password = request.POST['txtPassword']
        result = None
        try:
            tmpUser = UserInfo.objects.get(username=username, password=password)
            tmpUser = model_to_dict(tmpUser) # Model to dictionary
            request.session['CurrentUser']=tmpUser # Object of type UserInfo is not JSON serializable
            print("Login "+str(request.session['CurrentUser']))
            result = True
        except:
            result = False

        if result == True:
            return redirect('/index')
        else:
            return redirect('/')

def new(request):
    if request.method =='GET':
        # get method - default
        print("New " + str(request.session['CurrentUser']))
        cUser = request.session['CurrentUser'];
        return render(request, 'epanel/new.html', {'cuser':cUser})
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
        # receive id and search record based on id
        id = int(request.GET['id'])
        tmpUser = UserInfo.objects.get(id=id)
        # send tmpUser to display on template
        print("Edit "+str(request.session['CurrentUser']))
        return render(request, 'epanel/edit.html', {'user':tmpUser})
    elif request.method=='POST':
        # receive values from edit form
        id = int(request.POST['txtId'])
        user = request.POST['txtUser']
        password = request.POST['txtPassword']
        name = request.POST['txtFullName']
        email = request.POST['txtEmail']
        # search record and update
        tmpUser = UserInfo.objects.get(id = id)
        # set new values
        tmpUser.username=user
        tmpUser.password=password
        tmpUser.fullname=name
        tmpUser.email=email
        # save changes/update
        tmpUser.save()
        return redirect('/')

def delete(request):
    if request.method=='GET':
        id = int(request.GET['id'])
        # search and send to delete form
        tmpUser = UserInfo.objects.get(id=id)
        print("Delete "+str(request.session['CurrentUser']))
        return render(request, 'epanel/delete.html', {'user': tmpUser})
    elif request.method == 'POST':
        # receive id
        id = int(request.POST['txtId'])
        # Record search
        tmpUser = UserInfo.objects.get(id=id)
        tmpUser.delete()
        return redirect('/')