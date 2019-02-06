import requests
import sqlalchemy as sa
from himydata.hmd.api import hmddataset
import pandas as pd

class Dataset(object):

    # name = None

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

    def get_dataset_as_dataframe(self):
        """
        :param name: dataset name
        :return: pandas dataframe
        """
        if not self.engine.has_table(self.conf['name']):
            return None

        return pd.read_sql("SELECT * FROM %s" % self.conf['name'], self.engine)

    def get_dataset_sql_engine(self):
        """
        :param name: dataset name
        :return: SQLAlchemy engine
        """
        if not self.engine.has_table(self.conf['name']):
            return None

        return self.engine

    def get_dataset_table(self):
        """
        :param name: dataset name
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
        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        ResultProxy.close()
        return ResultSet

    def query_as_dataframe(self, query):
        """
        :param query: SqlAlchemy query
        :return: pandas dataframe with query results
        """
        if not self.engine.has_table(self.conf['name']):
            return None

        return pd.read_sql_query(query, self.engine)
