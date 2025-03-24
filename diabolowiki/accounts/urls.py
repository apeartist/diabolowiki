from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.register, name='account'),
    path('login', views.login, name='login'),
    #path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
]