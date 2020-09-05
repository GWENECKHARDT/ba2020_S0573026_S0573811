from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_list, name='list_list'),
    path('todo/<int:pk>/', views.list_detail, name='list_detail'),
    path('todo/new/', views.list_new, name='list_new'),
    path('todo/<int:pk>/edit/', views.list_edit, name='list_edit'),
    path('accounts/register', views.register, name='register'),
    path('todo/<pk>/remove/', views.list_remove, name='list_remove'),
    path('todo/tododetails', views.todo_details, name='todo_details'),
    path('todo/<int:pk>/todoedit/', views.todo_edit, name='todo_edit'),
    path('todo/todonew/', views.todo_new, name='todo_new'),
    path('todo/<int:pk>/todos/', views.add_todo_to_list, name='add_todo_to_list'),
    path('todo/<int:pk>/approve/', views.todo_approve, name='todo_approve'),
    path('todo/<int:pk>/remove/', views.todo_remove, name='todo_remove'),
]

