from django.urls import path
from .views import *

urlpatterns = [
	path('', CustomUserViewSet.as_view({
		'get' : 'list',
		'post': 'create'
	})),
	path('<int:pk>', CustomUserViewSet.as_view({
		'get'   : 'retrieve',
		'put'   : 'update',
		'delete': 'destroy',
	})),
	path('freelancers/', FreelancerViewSet.as_view({
		'get' : 'list',
		'post': 'create'
	})),
	path('freelancers/<int:pk>', FreelancerViewSet.as_view({
		'get'   : 'retrieve',
		'put'   : 'update',
		'delete': 'destroy',
	})),
	path('customers/', CustomerViewSet.as_view({
		'get' : 'list',
		'post': 'create'
	})),
	path('customers/<int:pk>', CustomerViewSet.as_view({
		'get'   : 'retrieve',
		'put'   : 'update',
		'delete': 'destroy',
	})),
	path('reviews/', ReviewViewSet.as_view({
		'get' : 'list',
		'post': 'create'
	})),
	path('reviews/<int:pk>', ReviewViewSet.as_view({
		'get'   : 'retrieve',
		'put'   : 'update',
		'delete': 'destroy',
	})),
]
