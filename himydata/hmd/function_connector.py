from himydata.hmd.api import hmdapi
from himydata.hmd.api import hmdfunction, hmddataset
from himydata.hmd.hmd_client import HmdClient
from himydata.hmd.utils import datasets, dashboards


class Connector(object):
	"""
	Connection done through a function. Certain fields are already forseen
	"""
	def __init__(self, event, host="http://api.himydata.com/v1/", client=HmdClient, **kwargs):

		data = event['data']
		integrations = data['integrations']
		api_token = data['user_token']

		self.client = client(api_token, host=host, **kwargs)

		self.hmd_dataset = hmddataset.API(api_token, service_url=host + "dataset")
		self.apis = hmdapi.API(api_token, service_url=host)
		self.functions = hmdfunction.API(api_token, service_url=host)

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
