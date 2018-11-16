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
        query : cassandra type query

        Returns:
            a JSON object of the schema, with the list of columns
        """
        rows = self.session.execute(query)
        return rows


    def get_rows(self, dataset_name, heads=None, limit=None):
        """
        Get rows from dataset. All if heads is none and only the heads if present
        Heads refers to the columns filtered, if None mentioned, shows all

        dataset_name : tha name of the dataset in question
        heads : list containg the columns of interest
        limit : limit the number of rows retrieved

        Returns:
            a JSON object of the schema, with the list of columns
        """
        # rows={"titi": "toto"}

         
        if heads:
            query ='SELECT %s FROM %s' % (str(heads), dataset_name)
        else:
            query ='SELECT * FROM %s' % (dataset_name)
        if limit:
            query += ' LIMIT %s' % limit

        rows =self.session.execute(query)

        return rows


    # Without defining a “secondary index” there is no way to search for values using a WHERE clause restricting on any other column.
    # def get_row_by_value(self, dataset_name, head, value, heads=None, limit=None):
    #     """
    #     Get rows from dataset where head = value
    #     Heads refers to the columns filtered, if None mentioned, shows all
    
    #     dataset_name : tha name of the dataset in question
    #     heads : list with columns of interest
    #     limit : limit the number of rows retrieved
    #     head : the column on which to do the filter
    #     value : the value to look for

    #     Returns:
    #         a JSON object of the schema, with the list of columns
    #     """
    #     # rows={"titi": "toto"}
    #     if heads:
    #         query = 'SELECT %s FROM %s WHERE %s = %s' % (str(heads), dataset_name, head, value)
    #     else:
    #         query = 'SELECT * FROM %s WHERE %s = %s' % (dataset_name, head, value)
    #     if limit:
    #         query += ' LIMIT %s' % limit

    #     rows =self.session.execute(query)

    #     return rows

    # todo queries like SELECT * FROM cycling.upcoming_calendar WHERE year=2015 AND month=06;

    def insert_row(self, dataset_name, heads, values):
        """
        Insert a row to the dataset
        requires the columns affected and its values

        dataset_name : tha name of the dataset in question
        heads : list with columns of interest
        values : list with values to insert. Has to have the same order as heads

        Returns:
            request response
        """
        if len(heads) != len(values):
            return "Check variables! Number of column names doesn't match the number of values!"

        req = self.session.execute(
            'INSERT INTO %s (%s) VALUES (%s)' % (dataset_name, str(heads), str(values)))
        return req



