from django.http.response import Http404
from django.shortcuts import render,redirect

from django.http  import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserUpdateForm, ProfileUpdateForm, ProjectUploadForm
from awards.models import Project,User
from django.contrib import messages

# Create your views here.
def home(request):
    projects = Project.objects.all()
    users = User.objects.all()
    return render(request, 'home.html', {"projects":projects, "users": users})

def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except ObjectDoesNotExist:
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

def profile(request):
    projects = request.user.profile.projects.all()
    return render(request, 'profile.html', {"projects":projects})

def update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Successfully updated your account!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'update.html', context)

def upload_project(request):
    users = User.objects.exclude(id=request.user.id)
    if request.method == "POST":
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.save()
            messages.success(request, f'Successfully uploaded your Project!')
            return redirect('index')
    else:
        form = ProjectUploadForm()
    return render(request, 'upload_project.html', {"form": form, "users": users})
