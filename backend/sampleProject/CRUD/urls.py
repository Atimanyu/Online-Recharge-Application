from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserApi),
    path('user/<int:id>/', views.UserApi),
    path('admins/', views.AdminApi),
    path('admin/<str:id>/', views.AdminApi),
]