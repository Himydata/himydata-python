import requests
from himydata.hmd.api import hmdfunction, hmddataset
from himydata.hmd.utils import datasets, dashboards
from himydata.hmd.api import hmdapi
from himydata.hmd.hmd_client import HmdClient
# serviceUrl = "http://localhost:8002/v1/"


class Connector(object):
	serviceUrl = "http://api.himydata.com/v1/"
	"""
	Connection done through a function. Certain fields are already forseen
	"""
	def __init__(self, event, host=serviceUrl, client=HmdClient, **kwargs):

		data = event['data']
		integrations = data['integrations']
		apiToken = data['user_token']

		self.client = client(apiToken, host=host, **kwargs)

		self.hmd_dataset = hmddataset.API(apiToken, serviceUrl=host+"dataset")
		self.apis = hmdapi.API(apiToken, serviceUrl=host)
		self.functions = hmdfunction.API(apiToken, serviceUrl=host)

	def dataset(self, name):
		"""

		:param name: dataset name
		:return: newly created class used mostly internally, and only for a function
		"""
		dataset = datasets.Dataset(self.hmd_dataset, name)
		return dataset

	def dashboard(self):
		"""
		:return:
		"""
		dashboard = dashboards.Dashboard()
		return dashboard
