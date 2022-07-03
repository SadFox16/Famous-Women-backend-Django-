from django.urls import path
from .views import WomenAPIList, WomenAPIUpdate, WomenAPIDestroy, RegisterView, LoginView, Logout, CategoryAPIUpdate, CategoryAPIList, WomenByCategory, AdminCategoryAPIList, AdminWomenAPIList, CategoryAPIDestroy


urlpatterns = [
    #общие маршруты для админа и простых юзеров
    path('login/', LoginView.as_view(), name='login_token'),
    path('register/', RegisterView.as_view(), name='register'),
    path(r'^logout/', Logout.as_view(), name='logout'),
    path('women/', WomenAPIList.as_view(), name='women'),
    path('category/<int:pk>/', WomenByCategory.as_view(), name='women_by_category'),
    #маршруты для админа
    path('adminwomen/', AdminWomenAPIList.as_view(), name='admin_women'),
    path('category/', AdminCategoryAPIList.as_view(), name='admin_category'),
    path('women/<int:pk>/', WomenAPIUpdate.as_view(), name='admin_women_update'),
    path('admincategory/<int:pk>/', CategoryAPIUpdate.as_view(), name='admin_category_update'),
    path('deletewomen/<int:pk>/', WomenAPIDestroy.as_view(), name='admin_women_delete'),
    path('deletecategory/<int:pk>/', CategoryAPIDestroy.as_view(), name='admin_women_delete'),
]