from django.urls import path
from .views import *

urlpatterns = [
    path('', BookmarkListView.as_view(), name ='list'),
    path('add', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='dtail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),

    # rest API view
    path('api/', ApiBookmarkList.as_view()),
    path('api/<int:pk>', ApiBookmarkDetailList.as_view()),
]