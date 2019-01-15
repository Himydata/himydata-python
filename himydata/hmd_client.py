import requests
import time

from himydata.api import hmdfunction, hmdapi, hmddataset

# inspired from https://github.com/gophish/api-client-python/blob/master/gophish/client.py

serviceUrl = "http://api.himydata.com/v1/"


class HmdClient(object):
    """ A standard HTTP REST client used by Gophish """
    apiToken = None

    def __init__(self, apiToken, host=serviceUrl, **kwargs):
        self.apiToken = apiToken
        self.host = host
        self._client_kwargs = kwargs

    def execute(self, method, path, **kwargs):
        """ Executes a request to a given endpoint, returning the result """

        url = "{}{}".format(self.host, path)
        kwargs.update(self._client_kwargs)
        response = requests.request(
            method, url, params={"apiToken": self.apiToken}, **kwargs)
        return response


class Hmd(object):
    """
    Ensure connection to Himydata
    """
    def __init__(self,
        apiToken,
        host=serviceUrl,
        client=HmdClient,
        **kwargs):
        self.client = client(apiToken, host=host, **kwargs)
        self.datasets = hmddataset.API(apiToken)
        self.apis = hmdapi.API(apiToken)
        self.functions = hmdfunction.API(apiToken)


    # apiKey = None
    # statusPollDelay = 0.5

    # def set_apiToken(self, apiKey):
    #   self.apiKey = apiKey

    # def set_service_url(self, serviceUrl):
    #   self.serviceUrl = serviceUrl

    # def _url(path):
    #     return serviceUrl + path

    # def run(self):
    #   dataset = hmddataset(self.apiKey, serviceUrl=self.serviceUrl)
    #   api_ref = hmdapi(self.apiKey, serviceUrl=self.serviceUrl)
    #   function = hmdfunction(self.apiKey, serviceUrl=self.serviceUrl)


    # def _wait_for_job_finish(self, consumer, createJobResponse):
    #     while True:
    #         statusResult = consumer.jobStatus(createJobResponse.jobId)

    #         # from JobStatus.cs
    #         finalStates = [201, 202, 203]

    #         for finalState in finalStates:
    #             if finalState == statusResult.jobStatus:
    #                 return statusResult
    #       time.sleep(self.statusPollDelay)
