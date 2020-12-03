import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class DaftHTTPSession(requests.Session):
    """
    Wrap a regular session to use a base URL and add a user-agent header
    """
    DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"

    def __init__(self, prefix_url=None, user_agent=None, *args, **kwargs):
        super(DaftHTTPSession, self).__init__(*args, **kwargs)
        self.prefix_url = prefix_url

        if not user_agent:
            user_agent = DaftHTTPSession.DEFAULT_USER_AGENT

        self.headers.update({'User-Agent': user_agent})

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.prefix_url, url)
        return super(DaftHTTPSession, self).request(method, url, *args, **kwargs)


class Daft():
    """
    Make requests to the Daft website and parse them for eearching later
    """
    BASE_URL = "https://www.daft.ie/"

    def __init__(self, user_agent=None):
        self.site = DaftHTTPSession(Daft.BASE_URL, user_agent=user_agent)

    def get(self, url, params=None):
        req = self.site.get(url, params=params)
        req.raise_for_status()

        parsed_content = BeautifulSoup(req.content, "html.parser")
        return parsed_content

    def post(self, url, params=None):
        req = self.site.post(url, params=params)
        req.raise_for_status()
        return req
