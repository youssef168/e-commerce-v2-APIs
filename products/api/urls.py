from django.urls import path
from products.api.views.get import *

urlpatterns = [
    path('featured/', get_featured, name='get_featured'),
]