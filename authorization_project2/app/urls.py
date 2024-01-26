from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/pass_change/', views.pass_change, name='pass_change'),
    path('profile/edit/pass_change2/', views.pass_change2, name='pass_change2'),
]