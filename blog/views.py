from django.contrib import messages
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



@login_required
def todo_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/todo_list.html', {'posts': posts})


@login_required
def todo_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/todo_detail.html', {'post': post})


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
