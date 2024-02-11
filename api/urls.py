from rest_framework import routers
from news.views import CategoryViewSet, NewsViewSet

router = routers.DefaultRouter()

router.register(r'category', CategoryViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    *router.urls
]