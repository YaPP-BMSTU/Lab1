from table import *

class Metrics(Table):
    def __init__(self, data, filter, col, filter_name="region"):
        super().__init__(data)
        self.filter = filter
        self.col = col
        self.filter_name = filter_name
        data = []
        for row in self.data:
            if row[self.filter_name] == filter:
                data.append(row)
        self.data = data

    def __str__(self):
        return super().__str__(self.data)

    #тут функции для метрик