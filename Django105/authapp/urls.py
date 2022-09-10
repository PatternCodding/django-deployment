from django.urls import path
from authapp import views

# template tagging
app_name = 'basic_app'

urlpatterns = [
    path('', views.index,name='index'),
    path('', views.index,name='index'),
    path('main/', views.main,name='main'),
    path('register/', views.register,name='register'),   
    path('user_login/', views.user_login,name='user_login'),   
]
