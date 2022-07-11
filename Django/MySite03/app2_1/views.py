from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'app2_1/index.html')


# http://127.0.0.1:8000/app2_1/getValues1?pid=1&name=raj&address=ktm
# http://127.0.0.1:8000/app2_1/getValues1?pid=1&name=raj&address=LAT
def getValues1(request):
    # receive process, and output
    pid = request.GET.get('pid') # receive value from url
    name = request.GET.get('name')
    address=request.GET['address']
    data = {'pid':pid,'name':name, 'address':address}
    # Write on data file (text file)
    # Insert on database table
    # Write on xml file
    # Write on init file
    # Write on pdf file
    str1 = "<h1>Personal Info</h1>"
    str1 =  str1+"ID : "+str(pid)+"<br/>";
    str1 = str1+ "NAME : "+name+"<br/>"
    str1 = str1 + "ADDRESS : " + address + "<br/>"
    return HttpResponse(str1)

def getValues2(request):
    pid = request.GET['txt1']
    name = request.GET['txt2']
    address = request.GET['txt3']

    str1 = "<h1>Personal Info</h1>"
    str1 = str1 + "ID : " + str(pid) + "<br/>";
    str1 = str1 + "NAME : " + name + "<br/>"
    str1 = str1 + "ADDRESS : " + address + "<br/>"
    return HttpResponse(str1)

def getValues3(request):
    pid = request.POST['txt1']
    name = request.POST['txt2']
    address = request.POST.get('txt3')

    str1 = "<h1>Personal Info</h1>"
    str1 = str1 + "ID : " + str(pid) + "<br/>";
    str1 = str1 + "NAME : " + name + "<br/>"
    str1 = str1 + "ADDRESS : " + address + "<br/>"
    return HttpResponse(str1)