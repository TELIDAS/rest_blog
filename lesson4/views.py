from datetime import datetime, timedelta
from random import randint
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from lesson4.models import ConfirmationCode
from rest_blog import settings


class RegisterAPIView(APIView):

    def get(self, request):
        send_mail(subject='New subject',
                  message='lorem ipsum',
                  from_email=settings.EMAIL_HOST,
                  recipient_list=['khabiev2002@gmail.com'])
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.create(username=username,
                                   password=password,
                                   is_active=False)
        user.save()
        code = randint(10000000000, 9999999999999999)
        confirmation_code = ConfirmationCode
        confirmation_code.code = str(code)
        confirmation_code.user = user
        confirmation_code.valid_until = datetime.now() + timedelta(minutes=20)
        confirmation_code.save()
        send_mail(subject='Code Confirmation',
                  message=f'http://127.0.0.1:8000/confirm/{code}',
                  from_email=settings.EMAIL_HOST,
                  recipient_list=['username'])
        return Response(status=status.HTTP_200_OK)


class ConfirmAPIView(APIView):
    def post(self, request):
        code = request.data.get('code')
        codes = ConfirmationCode.objects.get(code=code,
                                             valid_until__gte=datetime.now())
        user = codes.user
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)

class LoginApiView(APIView):
    def post(self, request):
        user = authenticate(username=username,
                            password=password)
        token = Token.objects.create(user=user)
        pass