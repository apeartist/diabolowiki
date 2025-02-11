from django.urls import path, include
from . import views

app_name = 'tricks'
urlpatterns = [
    path('<trickname>', views.trick, name='tricks.trickpage'),
    path('all', views.alltricks),
]