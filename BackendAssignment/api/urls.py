from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view(), name='register'),
    path('login/', views.UserLogIn.as_view(), name='login'),
    path('post_create/', views.PostCreateView.as_view(), name='post-create'),
    path('post_list/', views.PostListView.as_view(), name='post-list'),
]