import json, yaml, csv
from hygiene.util.common.helpers import _csv

class DataFormatter:
    def __init__(self, fmt=None, output_path=None, data=None):
        self.fmt = fmt
        self.data = data
        self.output_path = output_path

    def format(self):
        """Convert data to the specified target format"""
        if self.fmt is None:
            raise ValueError("Formatter declared without format!")

        elif self.fmt == 'json':
            if isinstance(self.data, str):
                try:
                    yaml_obj = yaml.safe_load(self.data)
                    json_str = json.dumps(yaml_obj)
                    return json_str
                except:
                    raise TypeError("Improper yaml structure, cannot be formatted")
            elif isinstance(self.data, (list, tuple, dict)):
                # Convert Python object to JSON string
                data = json.dumps(self.data)
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
            raise ValueError(f'Unsupported data type "{self.data}"')
        return data

