from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='prev'),
    path('profile/', views.profile, name='profile'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Reg.as_view(), name='register'),
    path('profile/received/', views.received, name='received'),
    path('profile/send/', views.send_message, name='send_message'),
    path('profile/sent/', views.sent, name='sent'),
    path('message/<int:pk>/', views.message_detail, name='message_detail'),
    path('message-history/', views.message_history, name='message_history'),
]
