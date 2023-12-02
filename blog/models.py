from django.db import models


class Post(models.Model):
    title = models.CharField(primary_key=True, max_length=1000)
    body = models.TextField()

    def __str__(self):
        return self.title

class Users(models.Model):
    user_name = models.CharField(primary_key=True, max_length=1000)
    password = models.TextField()
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_name

class Users_Auth(models.Model):
    user_name = models.CharField(primary_key=True, max_length=1000)
    authorized = models.IntegerField()

    def __str__(self):
        return self.user_name