from django.urls import path
from women import views


urlpatterns = [

    #общие маршруты для админа и простых юзеров
    path('auth/login/', views.LoginView.as_view(), name='login_token'),
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    #path(r'^logout/', views.Logout.as_view(), name='logout'),
    path('user/women/', views.WomenAPIList.as_view(), name='women'),
    #path('user/women/<int:pk>/', views.S.as_view(), name='single_women')
    path('user/category/', views.CategoryAPIList.as_view(), name='get_category_list'),
    path('user/category/<int:pk>/', views.WomenByCategory.as_view(), name='women_by_category'),

    #маршруты для админа
    path('admin/women/', views.AdminWomenAPIList.as_view(), name='admin_women'),
    path('admin/women/<int:pk>/', views.WomenAPIUpdate.as_view(), name='admin_women_update'),
    path('admin/category/', views.AdminCategoryAPIList.as_view(), name='admin_category'),
    path('admin/category/<int:pk>/', views.CategoryAPIUpdate.as_view(), name='admin_category_update'),
]