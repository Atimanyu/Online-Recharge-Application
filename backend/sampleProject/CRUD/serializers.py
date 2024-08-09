# myapp/serializers.py
from rest_framework import serializers
from .models import User, Admin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # or specify fields explicitly, e.g., ['id', 'name', 'email']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'  # or specify fields explicitly, e.g., ['id', 'name', 'role']
