from django.urls import path
from . import views

urlpatterns= [ 
    path('',views.mainpage,name='mainpage'),
    path('learnmore/', views.learnPage, name='learnPage'),
    path('chatButton/', views.chatButton, name='chatButton')
]