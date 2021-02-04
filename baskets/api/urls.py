from rest_framework import routers
from .views import BasketsViewSet

router = routers.SimpleRouter()
router.register('', BasketsViewSet)
 

urlpatterns = router.urls 


# urlpatterns = [
#     Path..................... 
# ]
# urlpatterns =+ router.urls     (if you want to add urls )