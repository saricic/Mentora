from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns= [ 
    path('',views.mainpage,name='mainpage'),
    path('learnmore/', views.learnPage, name='learnPage'),
    path('chatButton/', views.chatButton, name='chatButton'),
    path('login/', LoginView.as_view(template_name='login.html'), name='loginbutton'),
    path('logout/', LogoutView.as_view(next_page='mainpage'), name='logout'),
    
  

]