from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

from .models import User, Women, Category
from .permissions import IsAdminOrReadOnly
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer, WomenSerializer, CategorySerializer


#Регистрация, авторизация, аутентификация
class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(UserSerializer(serializer.instance).data, status=status.HTTP_200_OK)


class Logout(APIView):

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

#-----------------------------------------------------------------------------------------


#view для обычного юзера
#для возвращения списка записей по GET
class WomenAPIList(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )


#для возвращения списка категорий по GET
class CategoryAPIList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )


#для получения записей по конкретной категории
class WomenByCategory(generics.RetrieveAPIView, generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )
    queryset = Category.objects.all()
#-----------------------------------------------------------------------------------------


#view для админа
#для возвращения списка записей по GET и добавления новой записи по POST
class AdminWomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )


#для возвращения списка категорий по GET и добавления новой категории по POST
class AdminCategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )


#для обновления одной записи(только PUT или PATCH)
class WomenAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    #отправляем одну измененную запись клиенту(ленивый запрос)
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminUser,)


#для обновления одной категории(только PUT или PATCH)
class CategoryAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    #отправляем одну измененную категорию клиенту(ленивый запрос)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)
#-----------------------------------------------------------------------------------------

