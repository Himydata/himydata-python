import requests

class dataset(object):
    """
    A dataset on the HMD instance
    """


    def __init__(self, apiToken, serviceUrl="http://api.himydata.com/gateway/api/manage"):
        self.serviceUrl = serviceUrl
        self.apiToken = apiToken


    def datasetGet(self, name, data=None):
        '''
        :type name : name of the dataset
        
        :rtype json
        '''

        url = self.serviceUrl + ("/%s/"% name)

        response = requests.get(url, data=data, headers=self._getDefaultHeaders())
        return response

    # todo opn back
    # def datasetSchema(self, name, data=None):
    #     '''
    #     :type name : name of the dataset
        
    #     :rtype json
    #     '''

    #     url = self.serviceUrl + ("/%s/"% name)

    #     response = requests.get(url, data=data, headers=self._getDefaultHeaders())
    #     return response


    # todo on back
    def datasetUpdate(self, name, content):
        '''
        :type name : name of the dataset
        :type content : formated text with new code for dataset
        
        :rtype json
        '''

        req_data = {'name': name,
                    'content': content}

        url = self.serviceUrl + ("/%s/"% name)

        response = requests.put(url, data=req_data, headers=self._getDefaultHeaders())
        return response

    def datasetStatus(self, name, data=None):
        '''
        :type name : name of the dataset
        
        :rtype str
        '''

        url = self.serviceUrl + ("/%s/status/"% name)

        response = requests.post(url, data=data, headers=self._getDefaultHeaders())
        return response

    def datasetLogs(self, name, data=None):
        '''
        :type name : name of the dataset
        
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
