from django.db import models


class UserInfo(models.Model):
    # id = int, autoincrement, primary key -> auto add
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.id, self.username, self.password, self.fullname, self.email)