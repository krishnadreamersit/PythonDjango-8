from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import PersonForm
from app1.functions import handle_uploaded_file
from app1.models import Person

def home(request):
    # receive all records from database
    persons = Person.objects.all()
    return render(request, 'app1/index.html', {'persons':persons})


def index(request):
    if request.method == 'POST':
        person = PersonForm(request.POST, request.FILES)
        if person.is_valid():
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
        person = PersonForm()
        return render(request, "app1/form1.html", {'form':person})
