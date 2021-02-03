from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_app.serializers import UserSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

class UserCreate(APIView):

    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLogin(APIView):

    

    def post(self, request, format='json'):
        try:
            serializer = LoginSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

            user = serializer.validated_data

            token = Token.objects.get(user=user)

            response = {
                "status":"success",
                "token":token.key,
                "user" : UserSerializer(user).data
            }
            return Response (response , status=status.HTTP_202_ACCEPTED)
        
        except Exception as e:
            print(e)
            return Response({"errors" : "Something went wrong while saving User"}, status=status.HTTP_400_BAD_REQUEST)

    