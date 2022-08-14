from cgi import FieldStorage
from dataclasses import fields
from rest_framework import serializers
from .models import *

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','roll_number','name','place')
