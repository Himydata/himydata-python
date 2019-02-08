import requests


class API(object):
    """
    A dataset on the HMD instance
    """

    def __init__(self, api_token, service_url="http://api.himydata.com/v1/dataset"):
        self.service_url = service_url
        self.api_token = api_token

    def get(self, name, data=None):
        """
        Method calls the dataset Api, get the contents of the dataset.
        Response is paginated.
        :param name:
        :param data:
        :return: http response
        """
        url = self.service_url + ("/%s/" % name)

        response = requests.get(url, data=data, headers=self.__get_default_headers())
        return response

    def insert(self, name, data=None):
        """
        Method calls the dataset Api used to insert a row in the dataset.
        :param name:
        :param data:
        :return: http response
        """
        url = self.service_url + ("/%s/" % name)

        response = requests.put(url, data=data, headers=self.__get_default_headers())
        return response

    def update(self, name, data):
        """
        Method calls the dataset Api used to update a row in the dataset.
        :param name:
        :param data:
        :return: http response
        """
        url = self.service_url + ("/%s/" % name)

        response = requests.post(url, data=data, headers=self.__get_default_headers())
        return response

    # todo opn back
    # def datasetSchema(self, name, data=None):
    #     '''
    #     :type name : name of the dataset

    #     :rtype json
    #     '''

    #     url = self.service_url + ("/%s/"% name)

    #     response = requests.get(url, data=data, headers=self._getDefaultHeaders())
    #     return response

    def get_config(self, name):
        """
        Method returns the config to connect to the database where the dataset is stored.
        The config is in a format specific for SqlAlchemy engine
        :param name:
        :return: json type
        """
        url = self.service_url + ("/%s/checkConfig/" % name)

        response = requests.get(url, headers=self.__get_default_headers())
        return response.json()

    def status(self, name, data=None):
        """
        Method returns the status of the dataset
        :param name: name of the dataset
        :param data:
        :return: str
        """

        url = self.service_url + ("/%s/status/" % name)

        response = requests.post(url, data=data, headers=self.__get_default_headers())
        return response

    def logs(self, name, data=None):
        """
        Method returns logs for the dataset
        :param name: name of the dataset
        :param data:
        :return: str
        """
        url = self.service_url + ("/%s/debug/" % name)

        response = requests.post(url, data=data, headers=self.__get_default_headers())
        return response

    def __get_default_headers(self):
        """

        :return: json type
        """
        return {
            "accept": "application/json",
            "authorization": "Token " + self.api_token
        }
