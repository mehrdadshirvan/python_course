from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    # path('<int:month>', views.monthly_challenges_by_number),
    path('<str:month>', views.monthly_challenges, name='month-challenge')
]
