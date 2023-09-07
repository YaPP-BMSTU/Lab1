from table import *


class Metrics(Table):
    def __init__(self, table, filter_val, col, filter_name="region"):
        self.header = table.header
        self.filter = filter_val
        if int(col) > len(self.header):
            raise MyException('Error, column number is invalid')
        self.col = int(col)
        self.filter_name = filter_name
        data = []
        for row in table.data:
            if row[self.filter_name] == filter_val:
                data.append(row)
        self.data = data
        self.metric_data = self.get_metric_data()

    def get_metric_data(self):
        try:
            metric_data = []
            for row in self.data:
                val = row[self.header[self.col - 1]]
                if len(val) == 0:
                    continue
                metric_data.append(float(val))
            return metric_data
        except ValueError:
            raise MyException('Error, field contains strings')

    def max(self):
        try:
            data = self.metric_data
            mx = data[0]
            for val in data:
                if mx < val:
                    mx = val
            return mx
        except IndexError:
            raise MyException('Error, fields not found for finding metrics')

    def min(self):
        try:
            data = self.metric_data
            mn = data[0]
            for val in data:
                if mn > val:
                    mn = val
            return mn
        except IndexError:
            raise MyException('Error, fields not found for finding metrics')

    def median(self):
        try:
            data = sorted(self.metric_data)
            n = len(data)
            if n % 2 == 0:
                return (data[n // 2 - 1] + data[n // 2]) / 2
            else:
                return data[n // 2]
        except IndexError:
            raise MyException('Error, fields not found for finding metrics')

    def average(self):
        try:
            return sum(self.metric_data) / len(self.metric_data)
        except ZeroDivisionError:
            raise MyException('Error, fields not found for finding metrics')

    def percentile_table(self):
        try:
            data = sorted(self.metric_data)
            mx = len(str(data[0]))
            for i in range(1, len(data)):
                tmp = len(str(data[i]))
                if mx < tmp:
                    mx = tmp

            print("Percentile table:")
            for i in range(21):
                result = data[round(((5 * i)/100) * (len(data))) - 1 if i != 0 else 0]
                space1 = 4 - len(str(i * 5))
                space2 = mx + 2 - len(str(result))
                print(f'|{space1 * " "}{i * 5}|{space2 * " "}{result}|')
        except IndexError:
            raise MyException('Error, fields not found for finding metrics')