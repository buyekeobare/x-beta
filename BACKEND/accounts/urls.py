from django.urls import path
from .views import RegisterView, LoginView, SignupView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),  
]