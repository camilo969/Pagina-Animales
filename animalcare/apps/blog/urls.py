from django.urls import path, include
from . import views

urlpatterns=[
    #MAIN BLOG localhost:8000/blog
    path('',views.blog),
    #MAIN BLOG 2 localhost:8000/blog/post_list/
    path('post_list/',views.post_list),
    #VER POST localhost:8000/blog/post/n°post/
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #CREAR NUEVO POST localhost:8000/blog/post/new/
    path('post/new/', views.post_new, name='post_new'),
    #EDITAR POST YA CREADO localhost:8000/blog/post/n°post/edit
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]