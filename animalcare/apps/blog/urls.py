from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

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

    #Mostrar todos los api objetos -localhost:8000/blog/api
    path('api/', views.API_objects.as_view()),

    #Mostrar solo un api objeto    -localhost:8000/blog/api/n°
    path('api/<int:pk>/', views.API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)