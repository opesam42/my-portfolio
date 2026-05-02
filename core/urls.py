from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'core'

urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
    path('freelance/', views.FreelanceView.as_view(), name='freelance'),
    path('google9e1a13e84d1227be.html', views.google_verification),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]