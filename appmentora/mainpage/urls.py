from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from accounts.views import SignUpView


urlpatterns= [ 
    path('',views.mainpage,name='mainpage'),
    path('learnmore/', views.learnPage, name='learnPage'),
    path('chatButton/', views.chatButton, name='chatButton'),
    path('login/', LoginView.as_view(template_name='login.html'), name='loginbutton'),
    path('logout/', LogoutView.as_view(next_page='mainpage'), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('api/chat/', views.gemini_proxy, name='gemini-proxy'),
    
    
  

]