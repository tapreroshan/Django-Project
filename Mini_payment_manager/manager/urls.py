from django.urls import path
from . import views


urlpatterns = [
    path('users/',views.userlist),
    path('users/<int:id>/', views.user_detail, name="user_detail"),
    path('services/',views.ServiceListView.as_view()),
    
]
