# Python

from urllib.parse import urljoin


# Main Section

from requests import Session


class RelativePathSession(Session):
    base_url = None

    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url

    def request(self, method, relative_url, **kwargs):
        url = urljoin(self.base_url, relative_url)
        return super().request(method, url, **kwargs)


class Gateway:

    # Variable Section
    _session = None
    version = None
    status_code = None

    def __init__(self, api):
        self.host = urljoin(api, self.version)
        # print('[Gateway] host: {}'.format(host))
        self._session = RelativePathSession(self.host)

    def request(self, method, url, **kwargs):
        response = self._session.request(method, url, **kwargs)
        self.status_code = response.status_code
        print(response.content)
        return self.status_code, response.json() # response body
