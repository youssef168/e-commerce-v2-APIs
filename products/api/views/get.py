from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db.models import Avg

# django


# internals
from products.models import *
from products.serializers import ProductSerializer

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_featured(request):
    data = Product.objects.filter(is_featured=True)
    serializers = ProductSerializer(data, many=True)
    return Response({
        "data": serializers.data
    }, status=status.HTTP_200_OK)