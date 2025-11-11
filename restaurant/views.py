from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import BookingTable, MenuTable
from .serializers import BookingSerializer, MenuSerializer

def index(request):
    return render(request, 'index.html', {})

def sayHello(request):
 return HttpResponse('Hello World')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer    

class BookingView(generics.ListCreateAPIView):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializer

class SingleBookingItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializer        

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return HttpResponse({"message":"This view is protected"})