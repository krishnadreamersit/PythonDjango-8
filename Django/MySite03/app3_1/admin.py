from django.contrib import admin
from .models import Person
from .models import Student
from .models import PersonalInfo

# Register your models here.
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(PersonalInfo)
