from django.urls import path
from . import views

app_name = 'dms'

urlpatterns = [
    path('', views.home, name="database-home"),
    path('faculty/', views.faculty, name="database-faculty"),
]
