from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.

class RegisterView(APIView):
    def post(self, request, format = None):
        data = request.data
        try:
            user = User.objects.create(**data)
            token = Token.objects.get(user = user)
            return Response({'Token': str(token)})
        except Exception as e:
            return Response({'error': str(e)})
