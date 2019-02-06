import json

class Dashboard(object):
    def __init__(self):
        self.graphs = {}
        self.default_name = "a"

    def make_graph(self, dataframe, graph_type, name=None):
        """
        expects a dt with only two columns
        :param dataframe: pandas dataframe type
        :param graph_type: graph_type type : 'pie', 'bar', 'line'
        :param name: name to be shown on the graph, default is dynamic if non provided
        :return:
        """

        cols = dataframe.columns.tolist()
        if len(cols) == 2:
            c1 = cols[0]
            c2 = cols[1]
            graph_json = {
                'graph_type': graph_type.lower(),
                'graph_data': {
                    'datasets': [{'data': dataframe[c1].tolist()}],
                    'labels': dataframe[c2].tolist()
                }
            }
            if name:
                graph_json["name"] = name
            else:
                graph_json["name"] = '%s/%s' % (c1, c2)
        elif len(cols) == 1:
            c1 = cols[0]
            graph_json = {
                'graph_type': graph_type.lower(),
                'graph_data': {
                    'datasets': [{'data': dataframe[c1].tolist()}],
                    'labels': dataframe.index.tolist()
                }
            }
            if name:
                graph_json["name"] = name
            else:
                graph_json["name"] = '%s' % c1

        else:
            return "Not currently supporting graph creation from more than two columns. Please rewrite your query."
        return graph_json

    def add_table(self, table_name):
        self.graphs[table_name] = {}

    def add_graph_to_table(self, graph, table_name):
        n = str(self.default_name + self.default_name)
        self.graphs[table_name].update({n: graph})

    def ready(self):
        """return the graph dictionary as a json string """
        return str(json.dumps(self.graphs))
