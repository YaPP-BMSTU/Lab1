class CSVParser:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        try:
            with open(self.filename, 'r') as f:
                csv_string = f.read()
            return csv_string
        except FileNotFoundError:
            print(f"Error, file {self.filename} not found.")

    def parse_csv(self):
        csv_string = self.read_csv()
        data = []
        if csv_string:
            rows = csv_string.split('\n')
            headers = rows[0].split(',')
            for row in rows[1:]:
                if row:
                    values = row.split(',')
                    data.append(dict(zip(headers, values)))
        self.data = data
        return data