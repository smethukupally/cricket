"""Mcc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path,include, re_path
from cric.views import login_view, logout_view, register_view
from django.conf.urls import url
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^accounts/login/$', login_view, name='login'),
    re_path(r'^accounts/logout/$', logout_view, name='logout'),
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    path('', include('cric.urls')),

]
