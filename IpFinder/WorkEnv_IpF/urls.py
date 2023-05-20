from django.urls import path

from . import views

urlpatterns = [
    path("", views.searchIP, name="searchIP"),
    path("", views.searchIPfj, name="searchIPjsonfj"),
    path("", views.auth, name ="auth"),
    path("", views.api, name="api"),
]