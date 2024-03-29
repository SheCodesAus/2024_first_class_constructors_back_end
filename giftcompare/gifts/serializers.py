from rest_framework import serializers
from .models import Gift


class GiftSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Gift
        fields = [
            'id',
            'name',
            'description',
            'price',
            'img',
            'source_url',
            'is_featured',
            'categories'        
        ]