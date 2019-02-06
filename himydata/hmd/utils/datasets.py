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
        conf = eval(self.__get_config())
        engine = sa.create_engine(conf['config'])

        if not engine.has_table(conf['name']):
            return None

        return pd.read_sql("SELECT * FROM %s" % conf['name'], engine)

    def get_dataset_sql_engine(self):
        """
        :param name: dataset name
        :return: SQLAlchemy engine
        """
        conf = eval(self.__get_config())
        engine = sa.create_engine(conf['config'])

        if not engine.has_table(conf['name']):
            return None

        return engine

    def get_dataset_table(self):
        """
        :param name: dataset name
        :return: SQLAlchemy table object
        """
        conf = eval(self.__get_config())
        engine = sa.create_engine(conf['config'])

        if not engine.has_table(conf['name']):
            return None

        metadata = sa.MetaData()
        tabel = sa.Table(conf['name'], metadata, autoload=True, autoload_with=engine)

        return tabel

    def query_as_list(self, query):
        """
        :param name: dataset name
        :return: list with results
        """
        conf = eval(self.__get_config())
        engine = sa.create_engine(conf['config'])

        if not engine.has_table(conf['name']):
            return None

        connection = engine.connect()
        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        ResultProxy.close()
        return ResultSet

    def query_as_dataframe(self, query):
        """
        :param query: SqlAlchemy query
        :return: list with results
        """
        conf = eval(self.__get_config())
        engine = sa.create_engine(conf['config'])

        if not engine.has_table(conf['name']):
            return None

        return pd.read_sql_query(query, engine)
