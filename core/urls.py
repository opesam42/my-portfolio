from django.urls import path
from . import views


app_name = 'core'

urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
    path('google9e1a13e84d1227be.html', views.google_verification),
]