from django.urls import path, include
from . import views

app_name = 'tricks'
urlpatterns = [
    path('all', views.alltricks, name='tricks-all'),
    path('newtrick', views.newtrick, name='new-trick'),
    path('<trickname>', views.trick, name='tricks-page'),
    path('<trickname>/edit', views.edittrick, name='tricks-edit'),
]