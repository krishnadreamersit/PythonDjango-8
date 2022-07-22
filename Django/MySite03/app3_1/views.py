from django.shortcuts import render
from django.http import HttpResponse
from app3_1.models import Student, Person, PersonalInfo
import csv

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


def migrate(request):
    file = open('./data/personal_data.csv')
    csv_reader = csv.reader(file)
    header = []
    header_row = next(csv_reader)
    # print(header_row)
    for row in csv_reader:
        # print(row[0], row[1], row[2], row[3], row[4])
        pinfo = PersonalInfo(id=row[0], first_name=row[1],
                             last_name=row[2], email=row[3], gender=row[4])
        pinfo.save()
    return HttpResponse("Data Migrate Successfully!")

def allpersons(request):
    return HttpResponse("Display all persons successfully")