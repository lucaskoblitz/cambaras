from django.urls import path, include
from . import views 

urlpatterns = [
	path('', views.home, name='home'),
	path('página_1', views.p1, name='p1'),
	path('página_2', views.p2, name='p2'),
	path('página_3', views.p3, name='p3'),
]