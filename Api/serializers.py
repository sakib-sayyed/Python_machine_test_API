from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Clients,Projects
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']
        
class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True,read_only=True)
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Projects
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = Clients
        fields = "__all__"