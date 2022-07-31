import django.http
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app4_1/index.html')

# settings.py
# 'django.contrib.sessions.middleware.SessionMiddleware' - Middleware
# 'django.contrib.sessions' - installed app

def add(request):
    # add value on Session
    data = "Broadway Infosys Nepal"
    request.session['var1'] = data # Store session-> key
    # add multiple values
        # add, update, delete - (list, tuple, set, dictionary, array)
    result = "Add value on session"
    context = {'message': result}
    return render(request, 'app4_1/index.html', context)

def display1(request):
    data = request.session['var1'] # Access
    return django.http.HttpResponse("Var1 = {}".format(data))

def display2(request):
    data = request.session['var1'] # Access
    return django.http.HttpResponse("Var1 = {}".format(data))

def update(request):
    request.session['var1'] = "BIN, KTM, NP" # Update
    return django.http.HttpResponse('var1 delete successfully')

def delete(request):
    # try, except, finally
    del request.session['var1'] # Delete
    return django.http.HttpResponse('var1 delete successfully')

