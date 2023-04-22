from django.urls import path

from accounts.views import RegisterView, LoginView, logout_view, UserDetail

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>', UserDetail.as_view(), name='user_detail'),
]
