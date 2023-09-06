from table import *

class Metrics(Table):
    def __init__(self, data, filter, col, filter_name="region"):
        super().__init__(data)
        self.filter = filter
        self.col = int(col)
        self.filter_name = filter_name
        data = []
        for row in self.data:
            if row[self.filter_name] == filter:
                data.append(row)
        self.data = data
        self.metric_data = self.get_metric_data()

    def get_metric_data(self):
        metric_data = []
        for row in self.data:
            metric_data.append(row[self.header[self.col - 1]])
        return metric_data

    def __str__(self):
        return super().__str__(self.data)

    #тут функции для метрик
    def max(self):
        try:
            data = self.metric_data
            mx = data[0]
            for val in data:
                if mx < val:
                    mx = val
            return mx
        except IndexError:
            return None

    def min(self):
        try:
            data = self.metric_data
            mn = data[0]
            for val in data:
                if mn > val:
                    mn = val
            return mn
        except IndexError:
            return None

    def median(self):
        pass

    def average(self):
        pass