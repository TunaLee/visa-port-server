# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework_nested import routers

# users
from visa_port.apps.users.api.views import UserViewSet


# Router
router = routers.SimpleRouter(trailing_slash=False)

router.register("user", UserViewSet)

app_name = 'api'
urlpatterns = [
                  path('', include("visa_port.apps.users.urls")),
              ] + router.urls
