from distutils.command.upload import upload
from django.db import models
from authy.models import User
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

# determine user's interests to provide the sutible products based on them
class Interests(models.Model):
    interest = models.CharField(max_length=255)



# this model represents a normal customer as well
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    interest = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='images/profile_pcis/')
    work_field = models.CharField(max_length=80)


class EmailContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)

class ContactNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(validators=[MaxLengthValidator(50, "contact Numbers Should Not Be Greater Than 50!")])