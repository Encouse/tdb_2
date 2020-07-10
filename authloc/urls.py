from rest_framework.authtoken import views
from django.urls import path
from . import views as locviews

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('register/', locviews.RegisterView.as_view()),
]
