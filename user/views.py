from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserCreateSerializer


class SendSMSCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        # Логика отправки SMS кода
        # ...
        return Response({'message': 'SMS code sent'}, status=status.HTTP_200_OK)


class VerifySMSCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        sms_code = request.data.get('sms_code')
        # Логика проверки SMS кода
        # ...
        return Response({'message': 'Phone number verified'}, status=status.HTTP_200_OK)


class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        # Проверка, что номер телефона верифицирован
        # ...
        return super().post(request, *args, **kwargs)
