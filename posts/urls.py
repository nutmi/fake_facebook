from rest_framework import routers
from .views import PostViewSet
router = routers.SimpleRouter()
router.register(r"posts", PostViewSet, basename="posts")
urlpatterns = router.urls
urlpatterns += []