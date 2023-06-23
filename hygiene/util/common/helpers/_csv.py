def _write_csv_rows(data, writer):
    if isinstance(data, list):
        if isinstance(data[0], dict):
            _write_csv_rows(data[0], writer)
    elif isinstance(data, dict):
        writer.writerow(data.keys())
        writer.writerow(list(data.values()))
    elif isinstance(data, int):
        writer.writerow([data])
    else:
        raise ValueError(f'Unsupported data type "{data}"')
