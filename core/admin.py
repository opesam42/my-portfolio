from django.contrib import admin
from .models import Article, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "date_added", "is_visible")
    ordering = ("order",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "date_added", "is_visible")
    ordering = ("order",)