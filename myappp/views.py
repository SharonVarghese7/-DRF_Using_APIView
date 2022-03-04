import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import userregister
from . serializers import userregisterSerializer
# Create your views here.
class registeredList(APIView):
    def get(self, request):
        register1=userregister.objects.all()
        serializer=userregisterSerializer(register1, many=True)
        return Response(serializer.data)   


    def post(self, request):
        serializer = userregisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)