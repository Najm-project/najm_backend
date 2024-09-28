from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
import random

from .serializers import UserRegistrationSerializer, VerifyCodeSerializer, UserLoginSerializer, \
    ChangePasswordSerializer, UpdateNameSerializer, RequestPasswordResetSerializer
from .eskiz import SendSmsApiWithEskiz, SUCCESS

User = get_user_model()


class UserRegistrationView(GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get('phone_number')
            verification_code = random.randint(1000, 9999)
            sms_api = SendSmsApiWithEskiz(message="Bu Eskiz dan test",
                                          phone=phone_number)
            print(sms_api)
            sms_status = sms_api.send()
            print(sms_status)

            if sms_status == SUCCESS:
                request.session[phone_number] = str(verification_code)
                serializer.save()
                return Response({'message': 'User registered successfully. Verification code sent.', 'code': verification_code},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Failed to send verification code.'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeView(GenericAPIView):
    serializer_class = VerifyCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = serializer.validated_data['verification_code']
            stored_code = request.session.get(phone_number)
            user = User.objects.get(phone_number=phone_number)

            if user.is_active:
                return Response({'message': 'User is already active.'}, status=status.HTTP_400_BAD_REQUEST)
            if stored_code == verification_code:
                try:
                    user.is_active = True
                    user.save()
                    request.session.pop(phone_number)
                    return Response({'message': 'Phone number verified successfully.'}, status=status.HTTP_200_OK)
                except User.DoesNotExist:
                    return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            user = serializer.context.get('user')
            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token

            data = {
                'access_token': str(access_token),
                "refresh_token": str(refresh_token)
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return response


class UpdateNameView(GenericAPIView):
    serializer_class = UpdateNameSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        if serializer.is_valid():
            user = request.user
            user.first_name = serializer.validated_data['first_name']
            user.last_name = serializer.validated_data['last_name']
            user.save()
            return Response({'message': 'Name updated successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'Password updated successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetView(GenericAPIView):
    serializer_class = RequestPasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = "1234"
            sms_api = SendSmsApiWithEskiz(message='Bu Eskiz dan test',
                                          phone=phone_number)
            sms_status = sms_api.send()

            if sms_status == SUCCESS:
                request.session[phone_number] = verification_code
                return Response({'message': 'Password reset code sent successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Failed to send password reset code.'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResendVerificationCodeView(GenericAPIView):
    serializer_class = RequestPasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = "1234"
            sms_api = SendSmsApiWithEskiz(message='Bu Eskiz dan test', phone=phone_number)
            sms_status = sms_api.send()

            if sms_status == SUCCESS:
                request.session[phone_number] = verification_code
                return Response({'message': 'Verification code resent successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Failed to resend verification code.'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
