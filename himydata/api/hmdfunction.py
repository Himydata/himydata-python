import requests


class API(object):
    """
    A dataset on the HMD instance
    """

    def __init__(self, apiToken, serviceUrl="http://api.himydata.com/v1/function"):
        self.serviceUrl = serviceUrl
        self.apiToken = apiToken

    def get(self, name, data=None):
        '''
        :type name : name of the function
        
        :rtype json
        '''

        url = self.serviceUrl + ("/%s/"% name)

        response = requests.get(url, data=data, headers=self._getDefaultHeaders())
        return response

    def update(self, name, content):
        '''
        :type name : name of the function
        :type content : formated text with new code for function
        
        :rtype json
        '''

        req_data = {'name': name,
                    'content': content}

        url = self.serviceUrl + ("/%s/"% name)

        response = requests.put(url, data=req_data, headers=self._getDefaultHeaders())
        return response

    def call(self, name, data=None):
        '''
        :type name : name of the function
        :type data : json data to pass on to the function when doing the call
        
        :rtype json
        '''

        url = self.serviceUrl + ("/%s/invoke/"% name)
        response = requests.post(url, data=data, headers=self._getDefaultHeaders())
        return response

    def status(self, name, data=None):
        '''
        :type name : name of the function
        
        :rtype str
        '''

        url = self.serviceUrl + ("/%s/status/"% name)

        response = requests.post(url, data=data, headers=self._getDefaultHeaders())
        return response

    def logs(self, name, data=None):
        '''
        :type name : name of the function
        
        :rtype str
        '''

        url = self.serviceUrl + ("/%s/debug/"% name)

        response = requests.post(url, data=data, headers=self._getDefaultHeaders())
        return response

    def _getDefaultHeaders(self):
        return {
            "accept": "application/json",
            "authorization": "Token " + self.apiToken
        }
