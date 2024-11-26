from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # Status Field
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # Post Fields
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()

    # Datetime Fields
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT,
    )

    # Default Sort Order
    class Meta:
        ordering = ('-published',)
        # adding a database index
        indexes = [
            models.Index(fields=['-published']),
        ]

    def __str__(self):
        return self.title