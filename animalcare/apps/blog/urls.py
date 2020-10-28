from django.urls import path
from django.urls import include
from . import views

urlpatterns=[
    #localhost:8000/blogmain
    path('blog/',views.blog),
]