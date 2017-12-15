from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Article
from .serializers import UserSerializer, ArticleSerializer


@permission_classes((IsAuthenticated, ))
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint para serializar usuarios.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@permission_classes((IsAuthenticatedOrReadOnly, ))
class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint para serializar artículos.
    Falta sobrescribir el get_queryset
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('created', 'title')
