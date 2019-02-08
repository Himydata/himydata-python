import requests


class API(object):
    """
    A dataset on the HMD instance
    """

    def __init__(self, api_token, service_url="http://api.himydata.com/v1/function"):
        self.service_url = service_url
        self.api_token = api_token

    def get(self, name, data=None):
        """
        :type name : name of the function
        :type data:
        :rtype json
        """

        url = self.service_url + ("/%s/" % name)

        response = requests.get(url, data=data, headers=self.__get_default_headers())
        return response

    def update(self, name, content):
        """
        :type name : name of the function
        :type content : formated text with new code for function
        
        :rtype json
        """

        req_data = {'name': name,
                    'content': content}

        url = self.service_url + ("/%s/" % name)

        response = requests.put(url, data=req_data, headers=self.__get_default_headers())
        return response

    def call(self, name, data=None):
        """
        :type name : name of the function
        :type data : json data to pass on to the function when doing the call
        
        :rtype json
        """

        url = self.service_url + ("/%s/invoke/" % name)
        response = requests.post(url, data=data, headers=self.__get_default_headers())
        return response

    def status(self, name, data=None):
        """
        :type name : name of the function
        :type data:
        :rtype str
        """

        url = self.service_url + ("/%s/status/" % name)

        response = requests.post(url, data=data, headers=self.__get_default_headers())
        return response

    def logs(self, name, data=None):
        """
        :type name : name of the function
        :type data:
        :rtype str
        """

        url = self.service_url + ("/%s/debug/" % name)

        response = requests.post(url, data=data, headers=self.__get_default_headers())
        return response

    def __get_default_headers(self):
        return {
            "accept": "application/json",
            "authorization": "Token " + self.api_token
        }
