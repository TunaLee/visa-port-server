# Django
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

# Third Party
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from bs4 import BeautifulSoup

# Local
from visa_port.apps.views.api.serializers.create import ExpirationViewCreateSerializer, ViewCreateSerializer
from visa_port.apps.views.models.index import ExpirationView
from visa_port.bases.api import mixins
from visa_port.bases.api.viewsets import GenericViewSet
from visa_port.modules.gateways.hi_korea import gateway
from visa_port.utils.api.response import Response
from visa_port.utils.decorators import create_decorator


# Class Section
class ExpirationViewViewSet(mixins.CreateModelMixin,
                            GenericViewSet):
    serializers = {
        'default': ExpirationViewCreateSerializer,
    }
    queryset = ExpirationView.objects.all()
    filter_backends = (DjangoFilterBackend,)

    @swagger_auto_schema(**create_decorator(title=_('비자 조회 - Guest')))
    def create(self, request, *args, **kwargs):
        try:

            response = gateway.get_expiration(request.data)
            soup = BeautifulSoup(response.text, 'html.parser')

            if soup.find('script', text=lambda text: text and "현재 체류중인 외국인이 아닙니다" in text):
                return Response(status=status.HTTP_400_BAD_REQUEST)

            visa_info = {
                'passport_no': None,
                'nationality': None,
                'birth_date': None,
                'visa_code': None,
                'expiration_date': None,
            }

            for row in soup.find_all('tr'):
                th = row.find('th')
                td = row.find('td')
                if th and td:
                    key = th.get_text(strip=True)
                    key_mapping = {
                        '여권번호': 'passport_no',
                        '국적': 'nationality',
                        '생년월일': 'birth_date',
                        '체류자격': 'visa_code',
                        '체류기간 만료일': 'expiration_date',
                    }
                    key = key_mapping.get(key, key)
                    value = td.get_text(strip=True).replace(' ', '')
                    visa_info[key] = value

            serializer = ViewCreateSerializer(data=visa_info)
            if serializer.is_valid(raise_exception=True):
                self.perform_create(serializer)
                return Response(
                    status=status.HTTP_201_CREATED,
                    code=201,
                    message=_('ok'),
                    data=serializer.data
                )
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                code=400,
                message=_('Invalid Data')
            )
