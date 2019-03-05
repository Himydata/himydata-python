import json


class Dashboard(object):
    def __init__(self):
        self.graphs = {}

    def make_graph(self, dataframe, graph_type='line', graph_size='md', name=None, order=None):
        """
        expects a dt with only two columns
        :param dataframe: pandas dataframe type
        :param graph_type: graph_type type : 'pie', 'bar', 'line'
                default : 'line'
        :param graph_size: graph_size type : 'lg', 'md', 'sm'
                default : 'md'
        :param name: name to be shown on the graph, default is dynamic if non provided
        :param order : order of the infos: [data, label] or [label, data]
        :return:
        """

        cols = dataframe.columns.tolist()
        if len(cols) == 2:
            c1 = cols[0]
            c2 = cols[1]
            graph_json = {
                'graph_type': graph_type.lower(),
                'graph_size': graph_size.lower(),
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
                'graph_size': graph_size.lower(),
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
            return {"error": "Not currently supporting graph creation from more than two columns. "
                             "Please rewrite your query."}
        return graph_json

    def add_section(self, name):
        """adds a section to the dashboard"""
        self.graphs[name] = {}

    def add_graph_to_section(self, graph, section, graph_name=None):
        """ add a graph as a sub-section of a dataset"""
        if not graph_name:
            graph_name = graph["name"]
        self.graphs[section].update({graph_name: graph})

    def ready(self):
        """return the graph dictionary as a json string """
        return str(json.dumps(self.graphs))
