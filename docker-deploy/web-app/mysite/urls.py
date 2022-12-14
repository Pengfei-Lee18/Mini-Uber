"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from login import views

urlpatterns = [
    path('', views.login),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('index/driverdetail/', views.driverdetail),
    path('index/profile/',views.profile),
    path('index/profile/edit/',views.editprofile),
    path('index/viewride<int:ride_id>/',views.viewride),
    path('index/owneredit<int:ride_id>/', views.owneredit),
    path('index/ownercancel<int:ride_id>/', views.ownercancel),
    path('index/shareredit<int:ride_id>/', views.shareredit),
    path('index/sharercancel<int:ride_id>/', views.sharercancel),
    path('index/complete<int:ride_id>/', views.complete),
    path('index/openride/',views.openride),
    path('index/shareride/',views.shareride),
    path('index/shareride/result<int:sharenumber>/',views.shareresult),
    path('index/driveride/',views.driveride),
    path('index/driveride/result<str:cartype>/',views.driveresult),
]
