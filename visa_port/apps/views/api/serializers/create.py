# Serializers
from visa_port.bases.api.serializers import ModelSerializer

# Models
from visa_port.apps.views.models.index import ExpirationView


# Class Section
class ExpirationViewCreateSerializer(ModelSerializer):
    class Meta:
        model = ExpirationView
        fields = ('passport_no', 'expiration_date', 'birth_date', 'nationality', 'visa_code')

