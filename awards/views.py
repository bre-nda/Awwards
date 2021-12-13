from django.http.response import Http404
from django.shortcuts import render

from django.http  import HttpResponse

from awards.models import Project,User

# Create your views here.
def home(request):
    projects = Project.objects.all()
    users = User.objects.all()
    return render(request, 'home.html', {"projects":projects, "users": users})

def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except:
        raise Http404()
    return render(request,"project.html", {"project":project})

def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_project(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message,"projects": searched_projects})
    else:
        message = "You haven't searched for any projects yet"
    return render(request, 'search.html', {'message': message})

