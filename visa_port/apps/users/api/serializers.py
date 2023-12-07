# Local
from visa_port.apps.users.models import User
from visa_port.bases.api.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('',)


class UserMeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('',)
