from django.contrib import messages
from django.contrib.auth import login
from django.utils import timezone
from .models import Post, ToDo
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ToDoForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def list_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'todolist/list_list.html', {'posts': posts})

@login_required
def list_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'todolist/list_detail.html', {'post': post})

@login_required
def list_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('list_list')


@login_required
def list_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('list_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'todolist/list_edit.html', {'form': form})


@login_required
def list_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('list_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'todolist/list_edit.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('list_list')

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "registration/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "registration/register.html",
                  context={"form":form})


def todo_new(request):
    if request.method == "TODO":
        form = ToDoForm(request.TODO)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.published_date = timezone.now()
            todo.save()
            return redirect('todo_details', pk=todo.pk)
    else:
        form = ToDoForm()
    return render(request, 'todolist/todo/todo_edit.html', {'form': form})


def todo_edit(request, pk):
    todo = get_object_or_404(Post, pk=pk)
    if request.method == "TODO":
        form = ToDoForm(request.TODO, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.published_date = timezone.now()
            todo.save()
            return redirect('list_detail', pk=todo.post.pk)
    else:
        form = ToDoForm(instance=todo)
    return render(request, 'todolist/todo/todo_edit.html', {'form': form})


@login_required
def todo_details(request):
    form = ToDoForm()
    return render(request, 'todolist/todo/todo_details.html', {'form':form})


@login_required
def todo_list(request):
    todos = ToDo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'todolist/todo/todo_list.html', {'todos': todos})


def add_todo_to_list(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.post = post
            todo.author = post.author
            todo.save()
            return redirect('list_detail', pk=post.pk)
    else:
        form = ToDoForm()
    return render(request, 'todolist/add_todo_to_list.html', {'form': form})


@login_required
def todo_approve(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.approve()
    return redirect('list_detail', pk=todo.post.pk)


@login_required
def todo_remove(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return redirect('list_detail', pk=todo.post.pk)

@login_required
def todo_closed(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'todolist/todo/todo_closed.html', {'post': post})


def anbs(request):
    return render(request, 'anbs/anb.html', {})

@login_required
def hilfe(request):
    return render(request, 'hilfe/hilfe.html', {})

@login_required
def hilfe_list(request):
    return render(request, 'hilfe/hilfe_list.html', {})

@login_required
def hilfe_todo(request):
    return render(request, 'hilfe/hilfe_todo.html', {})

@login_required
def hilfe_top(request):
    return render(request, 'hilfe/hilfe_top.html', {})