from email.policy import default
from django.db import models

from vendor.models import Category, Vendor

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_STATUS = (
        ('In Stock', "In Stock"),
        ("Not Available", "Not Available"),
    )
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    model = models.CharField(max_length=100)
    sku = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    about = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=PRODUCT_STATUS)
    img = models.ImageField(upload_to='images/product-pics/')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    stock_count = models.IntegerField(default=1)
    rating_count = models.IntegerField(default=0)
    review_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.pk}"