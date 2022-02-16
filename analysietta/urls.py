from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:alert>', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('auth/', views.auth, name="auth"),
]
