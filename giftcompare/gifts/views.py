from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Gift
from .serializers import GiftSerializer


class GiftList(APIView):
    def get(self, request):
        gifts = Gift.objects.all()
        serializer = GiftSerializer(gifts, many=True)
        return Response(serializer.data)