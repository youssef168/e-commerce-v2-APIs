from authy.models import User
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.middleware import csrf
import datetime 
# DRF Stuff
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import permissions

#simpleJwt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer

from .serializers import UserSerializer
# Create your views here.

def generate_token_for_user(user):
    """
    function return an access and refresh token for particular user

    """
    token = RefreshToken.for_user(user)

    return {
        'access': str(token.access_token),
        'refresh': str(token),
    }

class RegisterView(APIView):
    def post(self, request):
        # store the errors here
        messages = { "errors": [] }
        # get data from the response
        data = request.data
        csrf.get_token(request)
        print(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"])


        # extract the data from response data
        username = data.get("username")
        password = data.get("password")
        re_password = data.get("repassword")
        go_as = data.get("go_as")
        email = data.get("email")


        #check if user already exists with the name or email
        user_exists = User.objects.filter(email=email).exists()
        user_name = User.objects.filter(username=username).exists()
        response = Response()
        if user_exists:
            messages["errors"].append("User with this email already exists already exists")
        if user_name:
            messages["errors"].append("User with this username already exists, try with another")
        if len(username) == 0 or username == None:
            messages["errors"].append("Username can't be empty")
        if len(email) == 0 or email == None:
            messages["errors"].append("Email can't be empty")
        if  password == None:
            messages["errors"].append("Password can't be empty")
        if go_as == None:
            messages["errors"].append("Should User Chose Go As Option")
            
        if password != re_password:
            messages["errors"].append("Passwords Doesn't Match!, retype the confirm password and make sure that matches the password")
        if len(password) < 6:
            messages["errors"].append("Passwords Should be greater than 6")

        if len(messages['errors']) > 0:
            return Response({ "message": messages["errors"] }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create(
                full_name=username,
                email=email,
                password=make_password(password),
                role=go_as
            )      
            token =   generate_token_for_user(user)
            # response.set_cookie(
            #     key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
            #     value = token["access"],
            #     expires = str(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]),
            #     secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            #     httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            #     samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            # )
            # response.set_cookie(
            #     key="refresh",
            #     value=token['refresh'],
            #     expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            #     secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            #     httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            #     path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
            #     samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
            # )

            serializer = UserSerializer(user, many=False)

        except Exception as e:
            return Response({ "message": f"An Error Occured! {e}" }, status=status.HTTP_400_BAD_REQUEST)
        data = {
            "data": serializer.data,
            "access": token['access'],
            "refresh": token["refresh"]            
        }
        return Response(data, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny)

    def post(self, request, *args, **kwargs):
        response = Response()

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_execption=True)

        access = serializer.validated_data.get('access', None)

        refresh = serializer.validated_data.get('refresh', None)

        user = serializer.validated_data.get('user', None)

        if access is not None:
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=access,
                max_age=1000,
                secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
                samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
            )
            response.set_cookie(
                key="refresh",
                value=refresh,
                max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
                samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
            )

            response.data = {"message": "successfully logged in!", "data": user}
            response.status_code = status.HTTP_200_OK
        else:
            response.data = {"message": "something went wrong"}
            response.status_code = status.HTTP_400_BAD_REQUEST
        return response    




        

@api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
def get_profile(request):
    print("request:", request.COOKIES.get('access'))
    print(request.user)
    print(datetime.timedelta(days=30))
    # access = AccessToken(request.COOKIES.get('access'))

    # user = User.objects.get(id=access['user_id'])
    # serializer = UserSerializer(user, many=False).data
    # print("USER:", serializer)
    return Response({
        "data": "serializer"
    })