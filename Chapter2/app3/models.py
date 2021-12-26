from django.db import models

# Create your models here.

class Person(models.Model):
    fullname = models.CharField(max_length=50)
    contactaddress = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname+", "+self.contactaddress+", "+self.phone+", "+self.email