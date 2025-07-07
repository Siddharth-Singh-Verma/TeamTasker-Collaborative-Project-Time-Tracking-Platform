
from django.shortcuts import render,  redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView
from core.form import SignUpForm, ProjectForm, TaskForm, InviteMemberForm
from core.models import Project, Task
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally log in immediately:
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# For login/logout, we can use Django’s built-in views:
class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    # template_name can be omitted; after logout we redirect via LOGOUT_REDIRECT_URL
    pass



@login_required
def project_list(request):
    projects = request.user.projects.all()
    return render(request, 'project_list.html', {'projects': projects})


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.members.add(request.user)
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})



@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    tasks = project.tasks.all()
    invite_form = InviteMemberForm()

    if request.method == 'POST' and 'invite' in request.POST:
        invite_form = InviteMemberForm(request.POST)
        if invite_form.is_valid():
            user_to_add = invite_form.cleaned_data['user']
            project.members.add(user_to_add)
            return redirect('project_detail', project_id=project.id)

    if request.method == 'POST':
        form = TaskForm(request.POST, project=project)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = TaskForm(project=project,initial={'assignee': request.user})

    return render(request, 'project_detail.html', {
    'project': project,
    'tasks': tasks,
    'form': form,
    'invite_form': invite_form,
})

@login_required
def edit_task(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    task = get_object_or_404(Task, id=task_id, project=project)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, project=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = TaskForm(instance=task, project=project)

    return render(request, 'edit_task.html', {
        'form': form,
        'task': task,
        'project': project
    })


@login_required
def delete_task(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id, members=request.user)
    task = get_object_or_404(Task, id=task_id, project=project)

    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', project_id=project.id)

    return render(request, 'delete_task.html', {'task': task, 'project': project})
