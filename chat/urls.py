from rest_framework import routers
from .views import Room1to1ViewSet, MessageViewSet
router = routers.SimpleRouter()
router.register(r"room", Room1to1ViewSet, basename="room")
router.register(r"message", MessageViewSet, basename="message")
urlpatterns = router.urls
urlpatterns += []