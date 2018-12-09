from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('published', 'publish')
    )
    title = models.CharField(max_length=250)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
