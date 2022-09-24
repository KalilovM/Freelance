from django.urls import path
from .views import *

urlpatterns = [
	path('', OrderViewset.as_view({'get': 'list', 'post': 'create'})),
	path('<int:pk>', OrderViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]
