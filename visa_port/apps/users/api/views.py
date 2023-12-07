# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import action

# Third Party
from drf_yasg.utils import swagger_auto_schema

# Serializers
from visa_port.apps.users.api.serializers import UserMeSerializer
from visa_port.apps.users.decorators import me_decorator

# Models
from visa_port.apps.users.models import User

# Bases
from visa_port.bases.api.viewsets import GenericViewSet

# Utils
from visa_port.utils.api.response import Response


# Class Section
class UserViewSet(GenericViewSet):
    queryset = User.active.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**me_decorator(title=_(''), serializer=UserMeSerializer))
    @action(detail=False, methods=['get'])
    def me(self, request):
        return Response(
            status=status.HTTP_200_OK,
            code=200,
            message=_('ok'),
            data=UserMeSerializer(instance=request.user).data
        )
