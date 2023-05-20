"""
URL configuration for IpFinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from WorkEnv_IpF import views
from django.urls import path, re_path

# Список маршрутов
urlpatterns = [
    path("Auth/IpFider", views.searchIP),
    # API( JSON )
    path("apiFinder/<str:ip>", views.searchIPfj),
    # Маршрут инструкции к api
    path("api_manual/", views.api),
    # Маршрут к авторизации
    path("Auth/", views.auth),
    # Маршрут к главной странице
    path("IpFinder/", views.searchIP),
    path("", views.searchIP),
]
