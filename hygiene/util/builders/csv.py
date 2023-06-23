import csv

class Sequence:
    def __init__(self, columns):
        self.columns = columns

    def build(self, data, out):
        if self.columns is None:
            raise ValueError("Builder declared without columns to collate!")
        
        reader = csv.DictReader(data)

        # Create a new column with the concatenated values
        for row in reader:
            sequenced = " ###".join([f"{column}: {row[column]}" for column in self.columns])
            row['sequence'] = sequenced

            # Output the modified row to a new CSV file
            with open(f'{out}.csv', 'a', newline='') as f:
                writer = csv.DictWriter(out, fieldnames=reader.fieldnames + ['sequence'])
                if f.tell() == 0:
                    writer.writeheader()
                writer.writerow(row)
