from rest_framework import serializers
from vendor.serializers import CategorySerializer

from vendor.serializers import VendorSerializer
from .models import Product, Tag, Brand

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(many=False, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

