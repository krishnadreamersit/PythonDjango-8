from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'app2_1/index.html')


def getValues1(request):
    # receive process, and output
    pid = request.GET.get('pid') # receive value from url
    name = request.GET.get('name')
    str1 ="PID : "+str(pid)+"<br/>";
    str1 = str1+ "NAME : "+name+"<br/>"
    return HttpResponse(str1)