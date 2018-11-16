import requests

class Function(object):
    """
    A dataset on the HMD instance
    """


    def __init__(self, apiToken, serviceUrl="http://api.himydata.com/functions/manage"):
        self.serviceUrl = serviceUrl
        self.apiToken = apiToken


    def functionGet(self, name, data=None):
        '''
        :type name : name of the function
        
        :rtype json
        '''

        url = self.serviceUrl + ("/%s/"% name)

        response = requests.get(url, data=data, headers=self._getDefaultHeaders())
        return response

    def functionUpdate(self, name, content):
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

    def functionCall(self, name, data=None):
        '''
        :type name : name of the function
        :type data : json data to pass on to the function when doing the call
        
        :rtype json
        '''

        url = self.serviceUrl + ("/%s/invoke/"% name)
        response = requests.post(url, data=data, headers=self._getDefaultHeaders())
        return response

    def functionStatus(self, name, data=None):
        '''
        :type name : name of the function
        
        :rtype str
        '''

        url = self.serviceUrl + ("/%s/status/"% name)

        response = requests.post(url, data=data, headers=self._getDefaultHeaders())
        return response

    def functionLogs(self, name, data=None):
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
