from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm 


def project_create(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projects:project_list') 
    return render(request, 'projects/project_create.html', {'form': form})

def project_update(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('projects:project_detail', project_id=project.id)
    return render(request, 'projects/project_form.html', {'form': form, 'action': 'Update'})

def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('projects:project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})
