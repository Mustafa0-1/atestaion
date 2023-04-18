from rest_framework import routers

from retail.views import RetailViewSet

router = routers.SimpleRouter()
router.register('retail', RetailViewSet)

urlpatterns = []
urlpatterns += router.urls
