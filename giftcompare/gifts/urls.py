from django.urls import path
from . import views
urlpatterns = [
    path('gifts/', views.GiftList.as_view() ),
    path('gifts/<int:pk>/', views.GiftDetail.as_view() ),
]