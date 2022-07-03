from .models import  User, Women, Category
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    UserSerializer
    )

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
        #return HttpResponse('http://127.0.0.1:8000/login/')


# def get_question_count(question):
#     question_cnt = History.objects.filter(question=question).count()
#     return question_cnt
#
#
# def get_random_answer():
#    ids = Answers.objects.all().order_by('?').values_list('pk', flat=True)
#    pk = random.randint(0, len(ids)-1)
#    rand = Answers.objects.get(pk=ids[pk])
#    return rand
#
#
# def get_last_answer(question, user, answer_id):
#     answer = History.objects.filter(question=question, user=user).order_by('-created_date').first()
#     if answer and answer.id == answer_id:
#         return get_last_answer(question, user, get_random_answer().id)
#     return answer
#
#
# def get_answer(user, question):
#     answer = get_random_answer()
#     history = History(
#         user=user,
#         answer=get_random_answer(),
#         question=question,
#     )
#     history.save()
#     data = {
#         'answer': history.answer.answer,
#         'question_cnt': get_question_count(history.question)
#     }
#     return data


# class AnswerView(generics.CreateAPIView):
#     serializer_class = QuestionSerializer
#     permission_classes = (IsAuthenticated, )
#
#     def get_queryset(self):
#         return None
#
#     def post(self, request, *args, **kwargs):
#         print(request.__dict__)
#         serializer = self.get_serializer(data=request.data)
#         print(repr(request.data))
#         serializer.is_valid(raise_exception=True)
#         print(repr(serializer.validated_data))
#         data = get_answer(request.user, serializer.validated_data['question'])
#         print(repr(data))
#         return Response(data=data, status=status.HTTP_200_OK)
