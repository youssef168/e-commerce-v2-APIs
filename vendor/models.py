from django.db import models
from authy.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

class Vendor(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255, null=True)
    store_banner = models.ImageField(upload_to='vendors/banners/', null=True)
    store_pic = models.ImageField(upload_to='vendors/pics/', null=True)
    location = models.CharField(max_length=255, null=True)
    store_number = models.IntegerField(null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.pk}"

