from django.urls import path,include
from . import views

urlpatterns =[
    path("",views.index,name="index"),
    path("friend/<str:pk>",views.detail,name="detail"),
    path("friend/sent_msg/<str:pk>",views.sentMessages,name="sent_msg")
]