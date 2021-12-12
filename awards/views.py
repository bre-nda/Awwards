from django.shortcuts import render

from django.http  import HttpResponse

from awards.models import Project,User

# Create your views here.
def home(request):
    projects = Project.objects.all()
    users = User.objects.all()
    return render(request, 'home.html', {"projects":projects, "users": users})
