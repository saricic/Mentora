from django.urls import path
from . import views
from .views import clickButton

urlpatterns= [ 
    path('',views.mainpage,name='mainpage'),
    path('learnmore/',views.learnmorepage,name='learnmorepage'),
    #path('chat/',views.chatpage,name='chatpage'),
    path('chat/', views.chatbot, name='chatbot'),
    path('chat/',clickButton,name='chatButton'),
    
]