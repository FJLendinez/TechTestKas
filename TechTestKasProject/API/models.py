from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    """
    Una clase abstracta para gestionar de manera 
    automatica la creacion y modificacion de campos.
    """
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)


class Article(TimeStampedModel):
    """
    Modelo de artículos
    """
    title = models.TextField(max_length=150)
    slug = models.SlugField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(User,
                               related_name='articles')
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.title
