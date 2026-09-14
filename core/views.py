from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Project, Article


class HomeView(TemplateView):
    template_name = "index.html"


class ProjectsView(TemplateView):
    template_name = "projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(is_visible=True).order_by('order')
        return context


class BlogView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: order by a dedicated published_at field once articles store the real post date.
        context['articles'] = Article.objects.filter(is_visible=True).order_by('-date_added', 'order')
        return context


class FreelanceView(TemplateView):
    template_name = "freelance.html"


class MaintenanceView(TemplateView):
    template_name = "maintenance.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=503)


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def google_verification(request):
    content = "google-site-verification: google9e1a13e84d1227be.html"
    return HttpResponse(content, content_type="text/html")
