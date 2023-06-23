import json, yaml, csv
from hygiene.util.common.helpers import _csv

class DataFormatter:
    def __init__(self, fmt=None, output_path=None, data=None):
        self.fmt = fmt
        self.output_path = output_path
        self.data = data

    def format(self):
        """Convert data to the specified target format"""
        if self.fmt is None:
            raise ValueError("Formatter declared without format!")

        elif self.fmt in ['yaml', 'yml']:
            if isinstance(self.data, str):
                json_obj = json.loads(self.data)
                yaml_str = yaml.dump(json_obj, default_flow_style=False)
                return yaml_str
            elif isinstance(self.data, (list, tuple, dict)):
                # Convert Python object to YAML string
                data = yaml.dump(self.data, default_flow_style=False)
            else:
                raise ValueError(f'Unsupported data type "{self.data}"')
        elif self.fmt == 'csv':
            if isinstance(self.data, str):
                json_obj = json.loads(self.data)
                self.data = json_obj
            elif not isinstance(self.data, (list, tuple, dict)):
                raise ValueError(f'Unsupported data type "{self.data}"')
            # write data to CSV file
            with open(f'{self.output_path}.csv', mode='w') as csv_file:
                writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                _csv._write_csv_rows(self.data, writer)
                return csv_file.name
        else:
            raise ValueError(f'Unsupported target format "{self.fmt}"')
        
        return data