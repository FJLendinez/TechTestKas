from django.conf.urls import url, include
from rest_framework import routers
from .views import ArticleViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth', include('rest_framework.urls', namespace='rest_framework'))
]