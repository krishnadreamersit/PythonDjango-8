from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def receive_value1(request):
    val1 = request.GET.get('full_name')
    return HttpResponse("Full Name : "+str(val1))

def receive_value2(request, full_name):
    return HttpResponse("Full Name : "+str(full_name))

def display_form1(request):
    return render(request, "WebForm1.html")

def get_form1(request):
    full_name = request.GET.get("txt_name")
    return HttpResponse("Full Name : "+str(full_name))

def display_form2(request):
    return render(request, "WebForm2.html")

def get_form2(request):
    full_name = request.POST.get("txt_name")
    return HttpResponse("Full Name : "+str(full_name))

def display_form3(request):
    return render(request, 'WebForm3.html')

def get_form3(request):
    if request.method == 'GET':
        full_name = request.GET.get("txt_name")
        context = {'full_name': full_name, 'method': 'GET'}
        return render(request, 'DisplayValues3.html', context)
    elif request.method == 'POST':
        full_name = request.POST.get("txt_name")
        context = {'full_name': full_name, 'method': 'POST'}
        return render(request, 'DisplayValues3.html', context)