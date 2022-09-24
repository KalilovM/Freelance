from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class OrderViewset(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer