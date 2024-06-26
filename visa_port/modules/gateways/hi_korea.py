# Python
from urllib.parse import urljoin

# Django
from django.conf import settings

# Local
from visa_port.bases.modules.gateways import Gateway as BaseGateway

class HiKoreaGateway(BaseGateway):
    def __init__(self):
        super().__init__(base_url=urljoin(settings.HI_KOREA_URL, "/"))

    def get_expiration(self, data):
        path = 'info/CheckExprYmdByPassNoResult.pt'

        payload = {
            'passNo': data.get('passport_no'),
            'natCd': data.get('nationality_code'),
            'birthYmd': data.get('birth_date')
        }

        print('body : ', payload)

        return self.request(method="POST", path=path, data=payload)


gateway = HiKoreaGateway()
