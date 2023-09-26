"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main.views import show_main
from leisure.views import show_leisure
from education.views import show_education
from hobbi.views import show_hobbi
from achievement.views import show_achievement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leisure/', show_leisure, name='leisure'),
    path('', show_main, name='main'),
    path('education/', show_education, name='education'),
    path('hobbi/', show_hobbi, name='hobbi'),
    path('achievement/', show_achievement, name='achievement')
]
