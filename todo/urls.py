from django.urls import path
from . import views  

urlpatterns=[
    path('alltodos',views.ListTodo.as_view())
]