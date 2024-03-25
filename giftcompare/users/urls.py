from django.urls import path
from .views import CustomUserList, UserRegistrationView, CustomUserDetail

urlpatterns = [    
    path('users/', CustomUserList.as_view()),
    path('users/register/', UserRegistrationView.as_view(), name='user-register'),
    path('users/<int:pk>/', CustomUserDetail.as_view()),
    ]
