from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from .forms import PostForm

# Create your views here.
from .models import Post


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

def todo_list(request):
    return render(request, 'blog/todo_list.html', {})

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

def todo_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/todo_detail.html', {'todo': post})