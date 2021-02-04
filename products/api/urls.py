from rest_framework import routers
from .views import ProductsViewSet

router = routers.SimpleRouter()
router.register('', ProductsViewSet)
 

urlpatterns = router.urls