from django import forms

from .models import Post, ToDo


class PostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ('title', 'author', 'to',)

class ToDoForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ('text', 'author',)