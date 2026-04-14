from django.core.management.base import BaseCommand
from core.models import Project, Article

class Command(BaseCommand):
    help = 'Seeds the database with multiple projects and articles'

    def handle(self, *args, **kwargs):
        self.stdout.write("Cleaning old data...")
        # Optional: Clear existing data so you don't get duplicates
        Project.objects.all().delete()
        Article.objects.all().delete()

        # 1. Prepare your data in lists
        projects_to_create = [
            {
                "name": "FastAPI Microservice",
                "description": "High-concurrency API built for real-time data.",
                "github_url": "https://github.com/gbenga/fastapi-app",
            },
            {
                "name": "Django Real Estate Portal",
                "description": "A rental platform for Nigerian clients using DRF.",
                "github_url": "https://github.com/gbenga/lagos-rentals",
            },
            {
                "name": "Operating System Kernel Simulation",
                "description": "C-based simulation of CPU scheduling and memory management.",
                "github_url": "https://github.com/gbenga/os-sim",
            },
        ]

        articles_to_create = [
            {
                "title": "Understanding Python Concurrency",
                "description": "A deep dive into threading vs multiprocessing.",
                "external_url": "https://medium.com/p/123",
                "platform_name": "Medium",
            },
            {
                "title": "Why I Use PostgreSQL for Everything",
                "description": "The philosophy of relational data in a NoSQL world.",
                "external_url": "https://hashnode.com/p/456",
                "platform_name": "Hashnode",
            },
        ]

        # 2. Convert dictionaries to Model Objects
        project_objs = [Project(**data) for data in projects_to_create]
        article_objs = [Article(**data) for data in articles_to_create]

        # 3. Use bulk_create for maximum efficiency
        self.stdout.write("Executing bulk insert...")
        Project.objects.bulk_create(project_objs)
        Article.objects.bulk_create(article_objs)

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {len(project_objs)} projects and {len(article_objs)} articles!"))