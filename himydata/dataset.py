from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

class Dataset(object):
    """
    A dataset on the HMD instance
    """
    def __init__(self, datastore_settings, user=None):
        # self.username = datastore_settings.username
        # self.password = datastore_settings.password
        self.user = user
        # self.connection = connections['nosql']
        # self.session = self.connection.connection.session
        auth_provider = None

        if user:
            auth_provider = PlainTextAuthProvider(
                username='', password='')
        
        self.cluster = Cluster(datastore_settings['IPs'], auth_provider=auth_provider)
        self.session = self.cluster.connect(datastore_settings['keyspace'])

    ####################
    # Dataset metadata #
    ####################
    def get_schema(self):
        """
        Get the schema of the dataset

        Returns:
            a JSON object of the schema, with the list of columns
        """
        return (self.project_key, self.dataset_name)

    def execute(self, query):
        """
        Get the schema of the dataset

        Returns:
            a JSON object of the schema, with the list of columns
        """
        # rows={"titi": "toto"}
        rows = self.session.execute(query)
        return rows
        # for (name, age, email) in rows:
  #         print name, age, email

    def get_rows(self, dataset_name):
        """
        Get the schema of the dataset

        Returns:
            a JSON object of the schema, with the list of columns
        """
        # rows={"titi": "toto"}
        rows = self.session.execute(
            'SELECT address, city FROM ' + dataset_name)
        return rows
        # for (name, age, email) in rows:
  #         print name, age, email
