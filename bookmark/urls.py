from django.urls import path
from .views import *

urlpatterns = [
    path('', BookmarkListView.as_view(), name ='list'),
    path('add', BookmarkCreateView.as_view(), name='add')
]