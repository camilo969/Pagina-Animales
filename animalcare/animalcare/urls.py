"""animalcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    #localhost:8000/admin
    path('admin/', admin.site.urls),
    #localhost:8000/blog
    path('blog/',include('apps.blog.urls')),
    #localhost:8000
    path('',include('apps.mainpage.urls')),
    path('usuario/', include('apps.Usuario.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    #127.0.0.1:8000/usuario/registrar
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),

    #pwa
    path('', include('pwa.urls')),


    #Restet
    path('reset/password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', email_template_name='registration/password_reset_email.html'), name="password_reset"),
    path('reset/password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('reset/password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/password_reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

]
