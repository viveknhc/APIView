from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import Studentserializer
from rest_framework.response import Response
from rest_framework import status

from web import serializers


class StudentAPIView(APIView):
    
    def post(self,request,format=None):
        data = request.data
        serializer = Studentserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        student_obj = Student.object.get(pk=pk)
        serializer = Studentserializer(data = request.data,instance= student_obj)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"data updated successfully"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None):
        student_obj = Student.object.get(pk=pk)
        serializer = Studentserializer(data = request.data,instance= student_obj,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"data updated successfully"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk=None,format=None):
        if pk:
            student_obj = Student.object.get(pk=pk)
            serializer = Studentserializer(student_obj)
        else:
            queryset = Student.objects.all()
            serializer = Studentserializer(queryset,many=True)
        return Response(serializer.data)

    def delete(self,request,pk, format = None):
        Student.objects.get(pk=pk).delete()
        return Response({"Message":"Data Delete Successfully"})