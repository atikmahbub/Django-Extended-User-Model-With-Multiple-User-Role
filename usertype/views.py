from django.shortcuts import render
from rest_framework.views import APIView , View
from rest_framework import viewsets
from .serializer import HospitalRegisterSerializer
from .models import Hospital

# Create your views here


class HospitalRegisterView(viewsets.ModelViewSet):
    serializer_class =  HospitalRegisterSerializer
    queryset = Hospital.objects.all()
    http_method_names = ['post']