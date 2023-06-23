import csv
import yaml

class DataFormatter:
    def __init__(self, fmt=None, data=None):
        self.fmt = fmt
        self.data = data

    def format(self):
        """Convert data to the specified target format"""
        if self.fmt is None:
            raise ValueError("Formatter declared without format!")

        elif self.fmt == 'csv':
            if isinstance(self.data, str):
                try:
                    yaml_obj = yaml.safe_load(self.data)
                    if isinstance(yaml_obj, (list, tuple)):
                        header = set()
                        rows = []
                        for item in yaml_obj:
                            row = {}
                            for k, v in item.items():
                                if isinstance(v, (list, tuple)):
                                    row[k] = ','.join([str(i) for i in v])
                                elif isinstance(v, dict):
                                    row[k] = str(v)
                                    header.update(v.keys())
                                else:
                                    row[k] = str(v)
                            rows.append(row)

                        if len(header) > 0:
                            header = sorted(header)
                            writer = csv.DictWriter(open('output.csv', 'w'), fieldnames=list(rows[0].keys())+header)
                            writer.writeheader()
                        else:
                            writer = csv.DictWriter(open('output.csv', 'w'), fieldnames=list(rows[0].keys()))
                            writer.writeheader()
                        
                        for row in rows:
                            writer.writerow(row)
                        
                    elif isinstance(yaml_obj, dict):
                        writer = csv.DictWriter(open('output.csv', 'w'), fieldnames=list(yaml_obj.keys()))
                        writer.writeheader()
                        writer.writerow(yaml_obj)

                    return "Conversion to CSV successful"
                except:
                    raise TypeError("Improper YAML structure, cannot be formatted")

            else:
                raise ValueError("Unsupported data type")
        else:
            raise ValueError("Unsupported target format")
