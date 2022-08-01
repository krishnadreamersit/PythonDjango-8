from django.db import models


class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    filename = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)+", "+self.firstname+" "+self.lastname+", "+self.email+", "+self.filename
