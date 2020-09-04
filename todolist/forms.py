from django import forms

from .models import Post, ToDo


class PostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ('title', 'author',)

class ToDoForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ('title', 'text', 'author',)