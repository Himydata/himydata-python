import requests


class API(object):
    """
    A dataset on the HMD instance
    """

    def __init__(self, apiToken, serviceUrl="http://api.himydata.com/v1/dataset"):
        self.serviceUrl = serviceUrl
        self.apiToken = apiToken

    def get(self, name, data=None):
        '''
        :type name : name of the dataset
        
        :rtype json
        '''
        url = self.serviceUrl + ("/%s/" % name)

        response = requests.get(url, data=data, headers=self._getDefaultHeaders())
        return response

    def insert(self, name, data=None):
        '''
        :type name : name of the dataset

        :rtype json
        '''
        url = self.serviceUrl + ("/%s/" % name)

        response = requests.put(url, data=data, headers=self._getDefaultHeaders())
        return response

    def update(self, name, data):
        '''
        :type name : name of the dataset

        :rtype json
        '''
        url = self.serviceUrl + ("/%s/" % name)

        response = requests.post(url, data=data, headers=self._getDefaultHeaders())
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


    # todo  all following on back


    def status(self, name, data=None):
        '''
        :type name : name of the dataset
        
        :rtype str
        '''

        url = self.serviceUrl + ("/%s/status/"% name)

        response = requests.post(url, data=data, headers=self._getDefaultHeaders())
        return response

    def logs(self, name, data=None):
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
