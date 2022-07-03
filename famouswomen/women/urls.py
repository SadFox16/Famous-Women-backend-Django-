from django.urls import path
from .views import LoginView, RegisterView, Logout


urlpatterns = [
    path('login/', LoginView.as_view(), name='login_token'),
    path('register/', RegisterView.as_view(), name='register'),
    path(r'^logout/', Logout.as_view(), name='logout'),
    #path('logout/', Logout.as_view(), name='logout'),
    #path('/api-token-auth/logout', Logout.as_view(), name='logout')
    #path(r'^rest-auth/', Logout.as_view(), name='logout'),
    #path('getanswer/', AnswerView.as_view(), name='getanswer'),
]