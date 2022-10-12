from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('hapus/<int:pk>', hapus_task, name='hapus-task'),
    path('add/', add_task, name='add_task'),
    path('change-status/<int:pk>', change_status, name='change-status'),
    path('json', show_json, name='show_json'),
]
