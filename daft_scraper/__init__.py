import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib3.util import Retry


class DaftHTTPSession(requests.Session):
    """
    Wrap a regular session to use a base URL and add a user-agent header
    """
    DEFAULT_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

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

    def __init__(self, user_agent=None, enable_retries=True):
        self.site = DaftHTTPSession(Daft.BASE_URL, user_agent=user_agent)

        if enable_retries:
            retry_strategy = Retry(
                total=3,
                status_forcelist=[500, 502, 503, 504],
                backoff_factor=0.1
            )
            adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
            self.site.mount("https://", adapter)

    def get(self, url, params=None):
        req = self.site.get(url, params=params)
        req.raise_for_status()

        parsed_content = BeautifulSoup(req.content, "html.parser")
        return parsed_content

    def post(self, url, params=None):
        req = self.site.post(url, params=params)
        req.raise_for_status()
        return req
