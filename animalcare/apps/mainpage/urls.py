from django.urls import path, include
from . import views

urlpatterns=[
    #-------------------------------------------------
    #localhost:8000/mainpage
    path('index',views.index, name="index"),
    #localhost:8000/america
    path('america',views.america, name="america"),
    #localhost:8000/europa
    path('europa',views.europa, name="europa"),
    #localhost:8000/asia
    path('asia',views.asia, name="asia"),
    #localhost:8000/oceania
    path('oceania',views.oceania, name="oceania"),
    #localhost:8000/africa
    path('africa',views.africa, name="africa"),
    #localhost:8000/donaciones
    path('donaciones',views.donaciones, name="donaciones"),

    #-------------------------------------------------
]