from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.leadtrack, name="index"),
	path('register/', views.register, name="register"),
	path('logout', views.logout_request, name="logout"),
	path('login', views.login_request, name="login"),
	path('newlead', views.leadcreate, name="newlead"),
]