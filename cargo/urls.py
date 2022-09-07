from django.urls import path
from cargo.views import *


urlpatterns = [
    path('', index, name='index'),
    path('add', dist, name='dist')       
]
