from rest_framework import serializers
from .models import Category, Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        exclude = ('owner',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"