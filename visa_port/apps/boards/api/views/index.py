# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from com_duck.apps.boards.api.serializers.retreive import BoardRetrieveSerializer
from com_duck.apps.boards.models import Board
from com_duck.bases.api import mixins
from com_duck.bases.api.viewsets import GenericViewSet
from com_duck.utils.decorators import retrieve_decorator, destroy_decorator


# Class Section
class BoardViewSet(mixins.RetrieveModelMixin,
                   GenericViewSet):
    serializers = {
        'default': BoardRetrieveSerializer,
    }
    queryset = Board.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**retrieve_decorator(title=_('게시판 - Guest'), serializer=BoardRetrieveSerializer))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)


class BoardAdminViewSet(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        GenericViewSet):
    serializers = {
        'default': BoardCreateSerializer,
    }
    queryset = Board.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (BoardPermission,)

    @swagger_auto_schema(**token_patch_decorator(title='6. 게시판 - Admin'))
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(**destroy_decorator(title='6. 게시판 - Admin'))
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.posts.exists():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                code=400,
                message=_('Posts must be blank to delete.')
            )
        self.perform_destroy(instance)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            code=204,
            message=_('no content'),
        )
