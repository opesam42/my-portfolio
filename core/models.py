import uuid
from django.db import models

class TimeStampedModel(models.Model):
    # UUID as Primary Key
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Project(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    # Links
    demo_url = models.URLField(
        blank=True, 
        null=True, 
        help_text="Live link to the working application"
    )
    github_url = models.URLField(
        blank=True, 
        null=True, 
        help_text="Link to the source code"
    )
    writeup_url = models.URLField(
        blank=True, 
        null=True, 
        help_text="Link to a blog post explaining the technical details"
    )
    
    cover_image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.name

class Article(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    external_url = models.URLField(help_text="Link to the actual article")
    platform_name = models.CharField(max_length=50,)
    cover_image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.title