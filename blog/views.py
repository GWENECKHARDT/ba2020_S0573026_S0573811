from django.contrib import messages
from django.contrib.auth import login
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ToDoForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required
def todo_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/todo_list.html', {'posts': posts})


@login_required
def todo_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/todo_detail.html', {'post': post})


def todo_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('todo_list')


@login_required
def todo_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('todo_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/todo_edit.html', {'form': form})


@login_required
def todo_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('todo_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/todo_edit.html', {'form': form})

def todonew(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('tododetails', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/todoedit.html', {'form': form})

def todoedit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ToDoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('tododetails', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/todoedit.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('todo_list')

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


@login_required
def tododetails(request):
    form = PostForm()
    return render(request, 'blog/tododetails.html', {'form':form})