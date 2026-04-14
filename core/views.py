from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Project, Article

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Get the existing context (like 'view' and other defaults)
        context = super().get_context_data(**kwargs)
        
        # Add your backend data
        context['projects'] = Project.objects.filter(is_visible=True).order_by('-date_added')
        context['articles'] = Article.objects.filter(is_visible=True).order_by('-date_added')
        
        return context