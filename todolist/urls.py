from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_list, name='list_list'),
    path('list/<int:pk>/', views.list_detail, name='list_detail'),
    path('list/new/', views.list_new, name='list_new'),
    path('list/<int:pk>/edit/', views.list_edit, name='list_edit'),
    path('accounts/register', views.register, name='register'),
    path('anbs', views.anbs, name='anbs'),
    path('hilfe', views.hilfe, name='hilfe'),
    path('hilfe/hilfe_list', views.hilfe_list, name='hilfe_list'),
    path('hilfe/hilfe_todo', views.hilfe_todo, name='hilfe_todo'),
    path('hilfe/hilfe_top', views.hilfe_top, name='hilfe_top'),
    path('list/<pk>/remove/', views.list_remove, name='list_remove'),
    path('todo/<int:pk>/todoedit/', views.todo_edit, name='todo_edit'),
    path('todo/todonew/', views.todo_new, name='todo_new'),
    path('todo/<int:pk>/todos/', views.add_todo_to_list, name='add_todo_to_list'),
    path('todo/<int:pk>/approve/', views.todo_approve, name='todo_approve'),
    path('todo/<int:pk>/remove/', views.todo_remove, name='todo_remove'),
    path('todo/<int:pk>/closed', views.todo_closed, name='todo_closed'),

]
