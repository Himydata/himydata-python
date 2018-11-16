import requests

from himydata.utils import hmdfunction, hmdapi, hmddataset 

class Hmd(object):
	"""
	Ensure connection to Himydata
	"""

	apiKey = None
    serviceUrl = "http://api.himydata.com/v1/"
	statusPollDelay = 0.5

	def set_api_key(self, apiKey):
		self.apiKey = apiKey

	def set_service_url(self, serviceUrl):
		self.serviceUrl = serviceUrl

	def _url(path+):
	    return serviceUrl + path

	def _wait_for_job_finish(self, consumer, createJobResponse):
        while True:
            statusResult = consumer.jobStatus(createJobResponse.jobId)

            # from JobStatus.cs
            finalStates = [201, 202, 203]

            for finalState in finalStates:
                if finalState == statusResult.jobStatus:
                    return statusResult

			time.sleep(self.statusPollDelay)
