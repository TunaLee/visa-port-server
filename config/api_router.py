# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework_nested import routers

# users
from visa_port.apps.users.api.views import UserViewSet
from visa_port.apps.views.api.views.index import ExpirationViewViewSet

# Router
router = routers.SimpleRouter(trailing_slash=False)

router.register("user", UserViewSet)
router.register("view/expiration", ExpirationViewViewSet)

app_name = 'api'
urlpatterns = [
                  path('', include("visa_port.apps.users.urls")),
              ] + router.urls
