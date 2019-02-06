import requests


class API(object):
    """
    A dataset on the HMD instance
    """

    def __init__(self, apiToken, serviceUrl="http://api.himydata.com/v1/dataset"):
        self.serviceUrl = serviceUrl
        self.apiToken = apiToken

    def get(self, name, data=None):
        """
        Method calls the dataset Api, get the contents of the dataset.
        Response is paginated.
        :param name:
        :param data:
        :return: http response
        """
        url = self.serviceUrl + ("/%s/" % name)

        response = requests.get(url, data=data, headers=self._getDefaultHeaders())
        return response

    def insert(self, name, data=None):
        """
        Method calls the dataset Api used to insert a row in the dataset.
        :param name:
        :param data:
        :return: http response
        """
        url = self.serviceUrl + ("/%s/" % name)

        response = requests.put(url, data=data, headers=self._getDefaultHeaders())
        return response

    def update(self, name, data):
        """
        Method calls the dataset Api used to update a row in the dataset.
        :param name:
        :param data:
        :return: http response
        """
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

    def get_config(self, name):
        """
        Method returns the config to connect to the database where the dataset is stored.
        The config is in a format specific for SqlAlchemy engine
        :param name:
        :return: json type
        """
        url = self.serviceUrl + ("/%s/checkConfig/" % name)

        response = requests.get(url, headers=self._getDefaultHeaders())
        return response.json()

    def status(self, name, data=None):
        """
        Method returns the status of the dataset
        :param name: name of the dataset
        :param data:
        :return: str
        """

        url = self.serviceUrl + ("/%s/status/"% name)

        response = requests.post(url, data=data, headers=self._getDefaultHeaders())
        return response

    def logs(self, name, data=None):
        """
        Method returns logs for the dataset
        :param name: name of the dataset
        :param data:
        :return: str
        """
        url = self.serviceUrl + ("/%s/debug/"% name)

        response = requests.post(url, data=data, headers=self._getDefaultHeaders())
        return response

    def _getDefaultHeaders(self):
        """

        :return: json type
        """
        return {
            "accept": "application/json",
            "authorization": "Token " + self.apiToken
        }
