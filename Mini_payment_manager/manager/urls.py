from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.userlist, name='user_list'),
    path('users/<int:id>/', views.user_detail, name='user_detail'),
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/detail/', views.service_detail, name='service_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
