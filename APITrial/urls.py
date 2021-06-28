"""APITrial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from APitry import views
from APitry import router

urlpatterns = [
    #REST FRAMEWORKK URLS
    path('admin/', admin.site.urls),
    path('APitry/', views.MusicList),
    path('APitry/<int:pk>', views.MusicDetails),
    path('APitry/account/',include('account.urls'),name='account_url' ),

]
urlpatterns=format_suffix_patterns(urlpatterns)