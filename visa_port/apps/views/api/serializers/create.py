# Serializers
from rest_framework import serializers

from visa_port.apps.nationalities.models import Nationality
from visa_port.apps.visas.models import VisaCode
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


class ViewCreateSerializer(ModelSerializer):
    nationality = serializers.CharField(write_only=True, required=True)
    visa_code = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = ExpirationView
        fields = ('passport_no', 'birth_date', 'expiration_date', 'nationality', 'visa_code')

    def create(self, validated_data):
        nationality_data = validated_data.pop('nationality')
        visa_code_data = validated_data.pop('visa_code')

        nationality_instance= Nationality.objects.get(name=nationality_data)
        visa_code_instance = VisaCode.objects.get(name=visa_code_data)

        expiration_view = ExpirationView.objects.create(
            nationality=nationality_instance,
            visa_code=visa_code_instance,
            **validated_data
        )

        return expiration_view