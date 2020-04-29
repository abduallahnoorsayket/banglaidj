import jwt
from pprint import pprint
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView

# DRF packages
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

# DRF validation
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (

    TokenAuthentication,
    BasicAuthentication,
    SessionAuthentication,
)

# my app
from .models import JWTPayloadTrack
from .serializers import (

    JWTPayloadTrackSerializer,
)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello,  sayket !'}
        return Response(content)




class TakeJWTPayload(APIView):
    @csrf_exempt
    def get(self, request):
        print('HEADERS: ', request.headers)

        encoded_jwt = request.headers['Authorization']
        print('ENCODED JWT: ', encoded_jwt)

        if encoded_jwt:
            decoded_payloads = jwt.decode(encoded_jwt, 'SecretKeySayket', algorithms=['HS256'])
            print('DECODED: ', decoded_payloads)

            if decoded_payloads:
                saved_jwt_payloads = JWTPayloadTrack.objects.create(
                    username=decoded_payloads['username'],
                    password=decoded_payloads['password'],
                    iat=decoded_payloads['iat']
                )

                serialized_payload = JWTPayloadTrackSerializer(saved_jwt_payloads)

                return Response(serialized_payload.data, status=status.HTTP_201_CREATED)

            else:
                return Response({'message': 'decode not working!'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'message': 'jwt payload not found!'}, status=status.HTTP_404_NOT_FOUND)