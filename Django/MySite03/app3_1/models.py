from django.db import models

class Person(models.Model):
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname+", "+self.address

"""
    create model
    python manage.py makemigrations # script
    python manage.py migrate # run script
    register model on admin site
"""