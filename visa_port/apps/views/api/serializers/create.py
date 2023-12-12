# Serializers
from rest_framework import serializers

from visa_port.apps.nationalities.models import Nationality
from visa_port.bases.api.serializers import ModelSerializer

# Models
from visa_port.apps.views.models.index import ExpirationView

class ExpirationViewCreateSerializer(ModelSerializer):
    nationality_code = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = ExpirationView
        fields = ('passport_no', 'birth_date', 'nationality_code')

    def create(self, validated_data):
        nationality_code = validated_data.pop('nationality_code', None)
        if nationality_code:
            nationality = Nationality.objects.get(code=nationality_code)
            validated_data['nationality'] = nationality

        return super().create(validated_data)