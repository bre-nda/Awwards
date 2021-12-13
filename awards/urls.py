from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('project/<project_id>/',views.project,name ='project'),
]