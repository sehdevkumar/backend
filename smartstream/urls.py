from django.urls import path , include
from .views import *
urlpatterns = [
    path('api/',ProfileListApiView.as_view())
]
