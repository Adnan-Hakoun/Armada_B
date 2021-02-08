from rest_framework import routers
from .views import CategoriesViewSet

router = routers.SimpleRouter()
router.register('', CategoriesViewSet)
 

urlpatterns = router.urls 