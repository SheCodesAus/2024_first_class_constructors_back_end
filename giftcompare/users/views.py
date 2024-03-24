from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from giftcompare.permissions import IsAdminOrReadOnly, IsAdminOrSelf, IsAdminOrNothing

class CustomUserList(APIView):
    permission_classes = [IsAdminOrNothing]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomUserDetail(APIView):
    permission_classes = [IsAdminOrSelf]

    def get_object(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

        # Check object permissions
        self.check_object_permissions(self.request, user)

        return user

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)