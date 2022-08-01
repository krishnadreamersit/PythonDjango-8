from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import StudentForm
from app1.functions import handle_uploaded_file
from app1.models import Person


def home(request):
    return render(request, 'app1/index.html')


def index(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            firstName = request.POST['firstname']
            lastName = request.POST['lastname']
            email = request.POST['email']
            filename = request.FILES['file'].name
            print(firstName, lastName, email, filename)
            handle_uploaded_file(request.FILES['file'])
            p1 = Person()
            p1.firstname=firstName
            p1.lastname=lastName
            p1.email=email
            p1.filename=filename
            p1.save()
            print("File upload successfully")
            return redirect('/')
    else:
        student = StudentForm()
        return render(request, "app1/form1.html", {'form':student})
