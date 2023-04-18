import datetime

from django.db import models

# Create your models here.

class OurTeam(models.Model):
    rasm = models.TextField()
    ism = models.CharField(max_length=50)  # Ali Valiyev   VARCHAR(50)
    mansab = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return self.ism



class AboutUs(models.Model):
    type = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    info = models.TextField()
    rasm = models.TextField()

    def __str__(self):
        return self.title


class News(models.Model):
    rasm = models.TextField()
    type = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    sana = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.title




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class TXabar(models.Model):
    xabar = models.TextField()

    def __str__(self):
        return self.xabar

# Qachonki yangi model yaratilsa, yoki qaysidir modelga nimadir o'zgartirish kiritilsa birinchi qilinadigan ish:
# 1. python manage.py makemigrations
# 2. python manage.py migrate

