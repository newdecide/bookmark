from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bookmark

# rest API import
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookmarkSeralizer


# rest API
class ApiBookmarkList(ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSeralizer

class ApiBookmarkDetailList(RetrieveUpdateDestroyAPIView):
        queryset = Bookmark.objects.all()
        serializer_class = BookmarkSeralizer


# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    # 페이징 처리 추가
    paginate_by = 3


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields =['site_name', 'url']
    success_url = reverse_lazy('list')


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('list')


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')

