from django.contrib import admin
from django.urls import path
from compiler import views
urlpatterns = [
    path('questions',views.questions),
    path('problem/<str:title>/<str:id>',views.code),
    path('compile',views.compile),
    path('submit',views.submit_code),
    path('test',views.auth_test),

]
