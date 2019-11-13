from .models import Bookmark
from rest_framework import serializers

class BookmarkSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'


