from django.db import models

class Person(models.Model):
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)+", "+self.fullname+", "+self.address


class Student(models.Model):
    sid = models.IntegerField()
    fullname = models.CharField(max_length=50)
    standard = models.CharField(max_length=50)

    def __str__(self):
        return "{0}, {1}, {2}".format(self.sid, self.fullname, self.standard)

# python manage.py makemigrations
# python manage.py migrate

"""
    create model
    python manage.py makemigrations # script
    python manage.py migrate # run script
    register model on admin site
"""