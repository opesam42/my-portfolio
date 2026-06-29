from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Project, Article

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Get the existing context (like 'view' and other defaults)
        context = super().get_context_data(**kwargs)
        
        # Add your backend data
        context['projects'] = Project.objects.filter(is_visible=True).order_by('order')
        context['articles'] = Article.objects.filter(is_visible=True).order_by('order')
        
        return context


class FreelanceView(TemplateView):
    template_name = "freelance.html"


class MaintenanceView(TemplateView):
    template_name = "maintenance.html"
    
    
def custom_404(request, exception):
    return render(request, '404.html', status=404)



def google_verification(request):
    content = "google-site-verification: google9e1a13e84d1227be.html" 
    return HttpResponse(content, content_type="text/html")