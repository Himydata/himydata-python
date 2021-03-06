import requests


class API(object):
    """
    An api on the HMD instance
    """

    def __init__(self, api_token, service_url="http://api.himydata.com/v1/gateway"):
        self.serviceUrl = service_url
        self.apiToken = api_token

    def get(self, name, data=None):
        """
        :type name : name of the apiReference
        :type data :
        :rtype json
        """

        url = self.serviceUrl + ("/%s/" % name)

        response = requests.get(url, data=data, headers=self._getDefaultHeaders())
        return response

    def call(self, name, data=None):
        """
        :type name : name of the apiReference
        :type data : json data to pass on to the apiReference when doing the call
        
        :rtype json
        """

        url = self.serviceUrl + ("/%s/execute/" % name)
        response = requests.post(url, data=data, headers=self._getDefaultHeaders())
        return response

    # todo on back
    # def apiReferenceUpdate(self, name, content):
    #     '''
    #     :type name : name of the apiReference
    #     :type content : formated text with new code for apiReference

    #     :rtype json
    #     '''

    #     req_data = {'name': name,
    #                 'content': content}

    #     url = self.service_url + ("/%s/"% name)

    #     response = requests.put(url, data=req_data, headers=self._getDefaultHeaders())
    #     return response

    # def apiReferenceStatus(self, name, data=None):
    #     '''
    #     :type name : name of the apiReference

    #     :rtype str
    #     '''

    #     url = self.service_url + ("/%s/status/"% name)

    #     response = requests.post(url, data=data, headers=self._getDefaultHeaders())
    #     return response

    # def apiReferenceLogs(self, name, data=None):
    #     '''
    #     :type name : name of the apiReference

    #     :rtype str
    #     '''

    #     url = self.service_url + ("/%s/debug/"% name)

    #     response = requests.post(url, data=data, headers=self._getDefaultHeaders())
    #     return response

    def _getDefaultHeaders(self):
        return {
            "accept": "application/json",
            "authorization": "Token " + self.apiToken
        }
