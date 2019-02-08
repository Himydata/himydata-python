import requests

from himydata.hmd.api import hmdapi
from himydata.hmd.api import hmdfunction, hmddataset


# inspired from https://github.com/gophish/api-client-python/blob/master/gophish/client.py


class HmdClient(object):
    """ A standard HTTP REST client used by Gophish """
    api_token = None

    def __init__(self,
                 api_token,
                 host="http://api.himydata.com/v1/",
                 **kwargs):
        self.api_token = api_token
        self.host = host
        self._client_kwargs = kwargs

    def execute(self, method, path, **kwargs):
        """ Executes a request to a given endpoint, returning the result """

        url = "{}{}".format(self.host, path)
        kwargs.update(self._client_kwargs)
        response = requests.request(
            method, url, params={"api_token": self.api_token}, **kwargs)
        return response


class Hmd(object):
    """
    Ensure connection to Himydata
    """
    def __init__(self,
                 api_token,
                 host="http://api.himydata.com/v1/",
                 client=HmdClient,
                 **kwargs):
        self.client = client(api_token, host=host, **kwargs)
        self.datasets = hmddataset.API(api_token)
        self.apis = hmdapi.API(api_token)
        self.functions = hmdfunction.API(api_token)
