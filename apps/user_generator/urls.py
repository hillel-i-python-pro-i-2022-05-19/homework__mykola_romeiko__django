from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_generator),
    path('<int:quantity>', views.user_generator)
]
