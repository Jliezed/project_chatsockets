from django.urls import path

from . import views

app_name = "chatapp"
urlpatterns = [
    path('', views.signup_page, name='signup'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<str:room_name>/', views.room, name='room'),
]