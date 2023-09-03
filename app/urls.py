from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/',views.signuppage, name = "signuppage"),
    path('login/', views.loginpage, name = "login"),
    path('logout', views.logoutpage, name= "logout")
    
]
