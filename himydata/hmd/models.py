from datetime import datetime
from dateutil.tz import tzlocal

import json as _json
import dateutil.parser


def parse_date(datestr):
    """ Parses an ISO 8601 formatted date """
    return dateutil.parser.parse(datestr)


class Model(object):
    def __init__(self):
        self._valid_properties = {}

    def as_dict(self):
        """ Returns a dict representation of the resource """
        result = {}
        for key in self._valid_properties:
            val = getattr(self, key)
            if isinstance(val, datetime):
                val = val.isoformat()
            # Parse custom classes
            elif val and not isinstance(val,
                                        (int, float, str, list, dict, bool)):
                val = val.as_dict()
            # Parse lists of objects
            elif isinstance(val, list):
                val = [e.as_dict() for e in val]
            # If it's a boolean, add it regardless of the value
            elif isinstance(val, bool):
                result[key] = val

            # Add it if it's not None
            if val:
                result[key] = val
        return result

    @classmethod
    def parse(cls, json):
        """Parse a JSON object into a model instance."""
        raise NotImplementedError


class Error(Exception, Model):
    _valid_properties = {'message': None, 'success': None, 'data': None}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.message

    def __repr__(self):
        return _json.dumps(self.as_dict())

    @classmethod
    def parse(cls, json):
        error = cls()
        for key, val in json.items():
            if key in cls._valid_properties:
                setattr(error, key, val)
        return error
