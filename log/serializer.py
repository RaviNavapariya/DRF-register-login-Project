from .models import User
from rest_framework import serializers

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','phone_number','password']

class UserLoginserializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()    