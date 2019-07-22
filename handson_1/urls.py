"""handson_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('auth',auth,name='auth'),
]


  kb0011106
  kb0000011
  kb0000012
  kb0000009
  kb0011109
  kb0000024
  kb0000029
  kb0000028
  kb0000016
  kb0000017
  kb0000003
  kb0000031
  kb0000022
  kb0000008
  kb0000032
  kb0000027
  kb0000004
  kb0011108
  kb0010006
  kb0010011
  kb0011105
  kb0000007
  kb0010013
  kb0000013
  kb0000018
  kb0000030
  kb0000014
  kb0000019
  kb0000015
  kb0011104
  kb0000020
  kb0010008
  kb0011110
  kb0000021
  kb0000026
  kb0010004
  kb0000006
  kb0000005
  kb0000010
  kb0000033
  kb0000001
  kb0000002
  kb0010003
  kb0000025
  kb0000023