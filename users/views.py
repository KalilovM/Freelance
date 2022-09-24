from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class CustomUserViewSet(viewsets.ModelViewSet):
	queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer


class FreelancerViewSet(viewsets.ModelViewSet):
	queryset = Freelancer.objects.all()
	serializer_class = FreelancerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer


class ReviewViewSet(viewsets.ModelViewSet):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer