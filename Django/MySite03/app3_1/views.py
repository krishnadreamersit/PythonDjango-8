from django.shortcuts import render
from django.http import HttpResponse
from app3_1.models import Student, Person

# Create your views here.
# root\urls.py
# path('admin/', admin.site.urls), # default admin panel
# user and password
# display admin panel
    # models/tables and records
    # CRUD

# how to create user/password to login admin panel?
    # default database to connect
    # make migrations # prepared python manage.py makemigratons
    # migrate # create # python manage.py migrate
    # python manage.py createsuperuser
        # user name
        # password
        # email
        # yes
    # http://127.0.0.1:8000/admin/ <enter>

# http://127.0.0.1:8000/app3_1/index <enter>
def index(request):
    # CRUD using model

    # C - Create/Insert Record
    # Style-1
    # p1 = Person(fullname='Bikki', address='Lat')
    # p1.save()

    # Style-2
    # p2 = Person()
    # p2.fullname='Keshor'
    # p2.address="Bhk"
    # p2.save()

    # R - Retrieve /Select
    persons = Person.objects.all()
    print(persons)
    context = {'persons': persons}

    # Search/Filter
    person = Person.objects.get(id=1)
    if(person):
        print(person)
    else:
        print("Not found")

    # U - Update/Edit
    # ?

    # D - Delete/Remove
    # ?
    
    return render(request, 'app3_1/index.html', context)