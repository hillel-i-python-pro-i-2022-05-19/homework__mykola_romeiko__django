from django.urls import path
from . import views

app_name = 'user_generator'

urlpatterns = [
    path('', views.user_generator, name='index'),
    path('<int:quantity>', views.user_generator)
]
