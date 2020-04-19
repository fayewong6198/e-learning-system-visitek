from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('logout/', views.logout, name='logout'),
    path('password/', views.change_password, name='change-password'),
    path('reset-password/', views.reset_password, name='reset-password'),
]
