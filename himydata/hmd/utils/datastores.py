import sqlalchemy as sa
import pandas as pd


class Datastore(object):

    def __init__(self, hmd_dataset, dataset_name):
        self.hmd_dataset = hmd_dataset
        self.conf = eval(self.__get_config(dataset_name))
        self.engine = sa.create_engine(self.conf['config'])

    def __get_config(self, dataset_name):
        """private class, used to return the config necessary to make a direct sqlAlchemy connection to the database"""
        return self.hmd_dataset.get_config(dataset_name)

    def get_sql_engine(self):
        """
        :return: SQLAlchemy engine
        """
        return self.engine

    def get_query_as_list(self, query):
        """
        :param query: SqlAlchemy query
        :return: list with results
        """
        connection = self.engine.connect()
        result_proxy = connection.execute(query)
        result_set = result_proxy.fetchall()
        result_proxy.close()
        return result_set

    def get_query_as_dataframe(self, query):
        """
        :param query: SqlAlchemy query
        :return: pandas dataframe with query results
        """
        return pd.read_sql_query(query, self.engine)
