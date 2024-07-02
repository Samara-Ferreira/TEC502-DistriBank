'''
Classe responsável por converter valores float para string e vice-versa.
'''

from werkzeug.routing import BaseConverter


class FloatConverter(BaseConverter):
    regex = r'-?\d+\.\d+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)
