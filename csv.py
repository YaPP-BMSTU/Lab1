import os
from exception import MyException


class Csv:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def read_csv(self):
        try:
            with open(self.filename, 'r') as f:
                csv_string = f.read()
            return csv_string
        except FileNotFoundError:
            raise MyException(f'Error, file {self.filename} not found.')

    def parse_csv(self, delimiter=','):
        csv_string = self.read_csv()
        data = []
        if csv_string:
            rows = csv_string.split('\n')
            headers = rows[0].split(delimiter)
            for row in rows[1:]:
                if row:
                    values = row.split(delimiter)
                    if len(values) != len(headers):
                        print("Error, invalid CSV format.")
                        raise MyException('Error, invalid CSV format.')
                    data.append(dict(zip(headers, values)))
            if not data:
                raise MyException('Error, no data found in CSV file.')
        self.data = data
        return data
