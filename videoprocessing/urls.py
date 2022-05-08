from django.urls import path
from .views import *


urlpatterns = [
    path('', VideoListView.as_view(), name='index'),
]