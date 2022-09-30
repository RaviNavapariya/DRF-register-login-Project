from.serializer import Userserializer,UserLoginserializer
from rest_framework_simplejwt.tokens import RefreshToken
from.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth import login



# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserSignupApiview(APIView):
    def get(self,request,format=None):
        data= User.objects.all()
        serializer = Userserializer(data,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = Userserializer(data= request.data)
        if serializer.is_valid():
            user=serializer.save()
            user.set_password(user.password)
            user.save()
            return Response (serializer.data,status = status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)    


class UserLoginApiview(APIView):
    def post( self,request):
        serializer = UserLoginserializer(data= request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']       
            password = serializer.validated_data['password']
            user= authenticate(email=email,password=password)
            if user is not None :
                login(request,user)
                token = get_tokens_for_user(user)
                return Response(token)
            return Response({'email and password Invalid'})    
        return Response(serializer.errors)    
