from django.shortcuts import render
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return Response({"detail": "Login successful"}, status=status.HTTP_200_OK)
    return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class ClientsListView(APIView):
    def get(self, request):
        clients = Clients.objects.all()
        serializer = ClientSerializer(clients, many=True)
        data = serializer.data
        for items in data:
            items.pop('projects',None)
        print(data)
        return Response(data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = serializer.save(created_by=request.user)
            
            # Formatting the response data
            return_data = {
                'id': client.id,
                'client_name': client.client_name,
                'created_at': client.created_at.isoformat(),
                'created_by': client.created_by.username  # Assuming User model has a username field
            }
            return Response(return_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDetail(APIView):
    def get_object(self, pk):
        try:
            return Clients.objects.get(pk=pk)
        except Clients.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            client = self.get_object(pk)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        except AttributeError:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectForClient(APIView):
    def post(self, request, pk):
        try:
            client = Clients.objects.get(pk=pk)
        except Clients.DoesNotExist:
            return Response({"message": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data.copy()
        data["client"] = client.id
        users_data = request.data.get('users', [])
        users = []
        for user_info in users_data:
            try:
                user = User.objects.get(pk=user_info['id'])
                users.append(user)
            except User.DoesNotExist:
                return Response({"message": f"User with ID {user_info['id']} not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            project = serializer.save(created_by=request.user)
            project.users.set(users)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProjects(APIView):
    def get(self, request):
        projects = Projects.objects.filter(users=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)