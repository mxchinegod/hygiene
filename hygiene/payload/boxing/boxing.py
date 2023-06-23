from hygiene.util.formatters.single import json, yaml
from hygiene.util.builders import csv
import os

class Payload:
    def __init__(self, data=None, path=None, fmt=None):
        self.data = data
        self.output_path = path
        self.fmt = fmt

    def deliver(self):
        if self.fmt == 'csv':
            form = csv.DataFormatter(fmt=self.fmt, data=self.data, output_path=os.path.abspath(self.output_path))
            with open(form.format(), 'r') as f:
                return f.readlines()
        elif isinstance(self.data, (dict, list)):
            form = json.DataFormatter(fmt=self.fmt, data=self.data)
            return form.format()
        elif isinstance(self.data, str):
            try:
                form = yaml.DataFormatter(fmt=self.fmt, data=dict(self.data))
            except:
                form = json.DataFormatter(fmt=self.fmt, data=self.data)
            return form.format()