from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Report
from .models import ReportResponse

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username','email', 'is_staff']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        #fields = ['message', 'author', 'supervisor']
        fields = '__all__'

class ReportResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportResponse
        fields = ['message','report','author']