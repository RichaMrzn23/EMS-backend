from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from  rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

# Create your views here.



@api_view(['GET','POST', 'DELETE'])
@permission_classes([AllowAny])
def Register(request, pk= None):#to get request from Urls
    password = request.data.get('password')
    hash_password = make_password(password)
    request.data['password'] = hash_password

    if request.method == 'GET':
        if pk is not None:
            try:
                users= User.objects.get(id=pk)
                serializer = UserSerializer(users)
                return Response(serializer.data, status = status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response('User not found', status = status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer( users, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
    

    if request.method =='POST':
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("User Created", status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        

    if request.method =='DELETE':
        if pk is not None:
            try:
                users = User.objects.get(pk=pk)
                users.delete()
                return Response("User Deleted!!!")

            except User.DoesNotExist:
                return Response('User not found', status = status.HTTP_404_NOT_FOUND)
            

@api_view(['POST'])
@permission_classes([AllowAny])
def Login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    role = request.data.get('role')

    user = authenticate(username = email, password = password, role = role)

    if user == None: 
        return Response('Invalid Credentials!!!', status = status.HTTP_400_BAD_REQUEST)

    else:
        token,_ = Token.objects.get_or_create(user=user)#returns two value token and boolean
        return Response(token.key)
            


                
        

        
            






