from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import authenticate,login,logout
from .account_no import create_account_no
from .models import CustomUser, Sube
from django.db import IntegrityError
from .serializers import CustomUserSerializer,SubeSerializer
from rest_framework import viewsets


class SubeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Sube.objects.all()
    serializer_class = SubeSerializer


class AllUsers(APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)



class UserLogin(APIView):
    def post(self,request):
        data = request.data
        username = data.get("username",False)
        password = data.get("password",False)

        if not (username and password):
            return Response("wrong username or password.")
        user = authenticate(username=username,password=password)

        login(request,user)
        return Response("Login Successful")


class UserLogout(APIView):
    def post(self, request):
        logout(request)
        return Response('Signed Out')


class RegisterUser(APIView):
    def post(self, request):
        data = request.data

        username = data.get("username")
        password = data.get("password")

        if not (username and password):
            return Response("Username or password not entered")

        account_no = create_account_no()


        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            account_no=account_no
        )
        user.save()

        login(request, user)
        serializer = CustomUserSerializer(user)

        return Response(serializer.data)

class AssignCustomerToBranch(APIView):

    permission_classes = [permissions.IsAdminUser]

    def put(self, request, *args, **kwargs):
        username = kwargs.get("name")
        data = request.data
        kod = data.get("kod", False)
        if not (kod and username):
            return Response("Şube Kodu veya kullanıcı Belirtilmedi!")

        try:
           Sube = Sube.objects.get(kod=kod)
        except Sube.DoesNotExist:
            return Response("Böyle bir şube bulunmamaktadır.")

        try:
                user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response("Böyle bir kullanıcı bulunmamaktadır.")

        user.Sube = Sube
        user.save()

        serializer = CustomUserSerializer(user)
        return Response(serializer.data)




class Deposit(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request): #Bakiyeyi görüntülemek için kullandı.
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request): #Bakiye ekledi ve bakiye güncelledi.
        user = request.user
        data = request.data
        amount = data.get("amount")
        user.balance = user.balance + int(amount)
        user.save()

        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


class WithDraw(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        data = request.data
        amount = data.get("amount")
        if not amount:
            return Response("amount not entered")

        if int(amount) > user.balance:
            return Response("insufficient balance")

        user.balance = user.balance - int(amount)
        user.save()

        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

class SendMoney(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, name):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        send_username = kwargs.get("name")
        user = request.user
        data = request.data
        amount = data.get("amount")
        if int(amount) > user.balance:
            return Response("insufficient balance")


        send_user = CustomUser.objects.get(username=send_username)
        user.balance = user.balance - amount
        send_user.balance = send_user.balance + amount
        user.save()
        send_user.save()

        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

