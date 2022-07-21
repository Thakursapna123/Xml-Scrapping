from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Register,loginserial,Profileserial,UserPasswordSerial,PasswordResetemail,UserpasswordResetSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
class Registerview(APIView):
    def post(self,request,format=None):
        serial=Register(data=request.data)
        if serial.is_valid(raise_exception=True):
            user=serial.save()
            return Response({'msg':"Account Created Successfully"},status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)


class Loginview(APIView):
    def post(self,request,format=None):
        ser=loginserial(data=request.data)
        if ser.is_valid(raise_exception=True):
            email=ser.data.get('email')
            password=ser.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg':'login succes'},status=status.HTTP_200_OK)
            else:
                return Response({'msg':'email or password in invalid'},status=status.HTTP_404_NOT_FOUND)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)



class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serail=Profileserial(request.user)
        return Response(serail.data,status=status.HTTP_200_OK)


class PasswordChange(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serial=UserPasswordSerial(data=request.data,context={'user':request.user})
        if serial.is_valid(raise_exception=True):
            return Response({'msg':'Password Change Successfully'},status=status.HTTP_200_OK)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    def post(self,request,format=None):
        serializer=PasswordResetemail(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Link send successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserPasswordResetSerial(APIView):
    def post(self,request,uid,token,format=None):
        serializer=UserpasswordResetSerializer(data=request.data,context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def index(request):
    stu=Student.objects.all()
    serail=StudentSerail(stu,many=True)
    return Response(serail.data,status=status.HTTP_200_OK)



@api_view(['POST'])
def create(request):
    data=request.data
    serial=StudentSerail(data=data)
    if serial.is_valid():
        serial.save()
        return Response(serial.data)
    else:
        return Response(serial.errors)


@api_view(['DELETE'])
def delete(request,id):
    try:
        student=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response("id not found")
    if request.method=="DELETE":
        Student.objects.get(id=id).delete()
        return Response({"msg":"Data deleted"}) 

@api_view(['PUT'])
def update(request,id):
    try:
        student=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response("id not found")
    if request.method=="PUT":
        data=request.data
        serial=StudentSerail(student,data=data)
        if serial.is_valid():
            serial.save()
            return Response({"msg":"Data Updated"})
        else:
            return Response(serial.errors)
