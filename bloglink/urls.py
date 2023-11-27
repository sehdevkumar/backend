from django.urls import path , include
from .views import *
urlpatterns = [
    path('api/',BlogView.as_view())
]
