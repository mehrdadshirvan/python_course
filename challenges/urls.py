from . import views
from django.urls import path

urlpatterns = [
    path('january', views.january),
    path('sunday', views.sunday),
]
