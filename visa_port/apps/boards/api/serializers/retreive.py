# Serializers
from com_duck.bases.api.serializers import ModelSerializer

# Models
from com_duck.apps.boards.models import Board


# Class Section
class BoardRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name', 'description', 'view_mode', 'type', 'read_permission', 'write_permission', 'is_active')
