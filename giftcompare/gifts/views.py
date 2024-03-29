from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Gift
from .serializers import GiftSerializer
from rest_framework import status, permissions
from giftcompare.permissions import IsAdminOrReadOnly
from django.db import transaction


class GiftList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        gifts = Gift.objects.all()
        try:
            serializer = GiftSerializer(gifts, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e) 

    
    def post(self, request):
        serializer=GiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GiftDetail(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, pk):
        return Gift.objects.get(pk=pk)

    def get(self, request, pk):
        try:
            gift = self.get_object(pk)
            serializer = GiftSerializer(gift)
            return Response(serializer.data)
        except Gift.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        gift = self.get_object(pk)
        serializer = GiftSerializer(instance = gift, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FeaturedGiftList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        gifts = Gift.objects.filter(is_featured = True)
        serializer = GiftSerializer(gifts, many=True)
        return Response(serializer.data)
        
    def put(self, request): 
        with transaction.atomic():
            gifts = Gift.objects.all()
            for gift in gifts:
                gift.is_featured = (gift.pk in request.data)
                gift.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    