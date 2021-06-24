from django.urls import path
from authentication import views
urlpatterns = [
    path('login',views.login_user),
    path('auth_test',views.auth_test),
    path('signup',views.signup_user),
]