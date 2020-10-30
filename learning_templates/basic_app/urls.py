from django.urls import path, include
from basic_app import views


# Template tagging
app_name = 'basic_app'  # Ask Django to look for the urls under basic_app

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]
