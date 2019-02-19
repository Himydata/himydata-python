import sqlalchemy as sa
import pandas as pd
from himydata.hmd.utils.datastores import Datastore


class Dataset(object):

    def __init__(self, hmd_dataset, name):
        """
        :param hmd_dataset: class Api of hmddataset
        :param name: dataset name
        """
        self.hmd_dataset = hmd_dataset
        self.name = name

        self.conf = eval(self.__get_config())
        self.engine = sa.create_engine(self.conf['config'])

    def set_name(self, name):
        """
        :param name: dataset name
        """
        self.name = name

    def __get_config(self):
        """private class, used to return the config necessary to make a direct sqlAlchemy connection to the database"""
        return self.hmd_dataset.get_config(self.name)

    def get_dataset_sql_name(self):
        """
        :return: dataset name as stored in database
        """
        if not self.engine.has_table(self.conf['name']):
            return None

        return self.conf['name']

    def get_dataset_as_dataframe(self):
        """
        :return: pandas dataframe
        """
        if not self.engine.has_table(self.conf['name']):
            return None

        return pd.read_sql("SELECT * FROM %s" % self.conf['name'], self.engine)

    def get_dataset_sql_engine(self):
        """
        :return: SQLAlchemy engine
        """
        if not self.engine.has_table(self.conf['name']):
            return None

        return self.engine

    def get_dataset_table(self):
        """
        :return: SQLAlchemy table object
        """
        if not self.engine.has_table(self.conf['name']):
            return None

        metadata = sa.MetaData()
        tabel = sa.Table(self.conf['name'], metadata, autoload=True, autoload_with=self.engine)

        return tabel

    def query_as_list(self, query):
        """
        :param query: SqlAlchemy query
        :return: list with results
        """
        if not self.engine.has_table(self.conf['name']):
            return None

        connection = self.engine.connect()
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        result_proxy.close()
        return result_set

    def query_as_dataframe(self, query):
        """
        :param query: SqlAlchemy query
        :return: pandas dataframe with query results
        """
        if not self.engine.has_table(self.conf['name']):
            return None

        return pd.read_sql_query(query, self.engine)

    def get_datastore(self):
        datastore = Datastore(self.hmd_dataset, self.name)
        return datastore
