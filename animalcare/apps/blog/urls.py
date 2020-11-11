from django.urls import path, include
from . import views

urlpatterns=[
    #localhost:8000/blog/
    path('',views.blog, name='post_list_ext'),
    
    path('post_list/',views.post_list),

    #localhost:8000/blog/post/<int:pk>/
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    #localhost:8000/blog/post/new/
    path('post/new/', views.post_new, name='post_new'),

    #localhost:8000/blog/post/<int:pk>/edit/
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # borrar una post
    path('post/<int:pk>/borrar_post/', views.borrar_post, name="borrar_post"),
]