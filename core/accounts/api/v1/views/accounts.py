from accounts.utils import send_email_thread
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers import (RegisterApiSerializer, CustomAuthTokenSerializer,
                           CustomTokenObtainPairSerializer, PasswordChangeSerializer)

User = get_user_model()


class RegisterApiView(GenericAPIView):
    serializer_class = RegisterApiSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email': serializer.validated_data.get('email'),
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        context = {
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        }
        return Response(context)


class LogoutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordApiView(GenericAPIView):
    model = User
    serializer_class = PasswordChangeSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user_object = self.request.user
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not user_object.check_password(serializer.data.get('old_password')):
                return Response(data={'old_password': 'wrong password'}, status=status.HTTP_400_BAD_REQUEST)
            user_object.set_password(serializer.data.get('new_password1'))
            user_object.save()
            return Response(data={'message': 'successfully password changed'}, status=status.HTTP_200_OK)
        return Response(data={'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TestEmailApiView(GenericAPIView):
    def get(self, request):
        self.email = 'danielsadri01@gmail.com'
        user_object = get_object_or_404(User, email=self.email)
        token = self.get_token_for_user(user_object)
        email_object = EmailMessage(
            template_name='send_email/send_email.html',
            context={'token': token},
            from_email='admin@gmail.com',
            to=[self.email],
        )
        send_email_thread(email_object)
        return Response(data='send email')

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
