from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Gift
from .serializers import GiftSerializer
from rest_framework import status


class GiftList(APIView):
    def get(self, request):
        gifts = Gift.objects.all()
        serializer = GiftSerializer(gifts, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=GiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)