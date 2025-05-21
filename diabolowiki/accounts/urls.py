from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.account),
    path('account/', views.account, name='account'),
    path('account/edit', views.edit_account, name='editaccount'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]