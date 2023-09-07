from exception import MyException

class Table:
    def __init__(self, data):
        self.data = data
        self.header = self.get_header()

    def get_header(self):
        keys = self.data[0].keys()
        return list(keys)

    def __str__(self):
        data = self.data
        result = ""
        header = self.header
        size_dict = {}

        for val in header:
            size_dict[val] = len(val)

        for row in data:
            for key, val in row.items():
                tmp = size_dict[key]
                size_dict[key] = max(tmp, len(val))

        space = len(data) // 10
        result += f'{space * " "}id|'
        for val in header:
            space = size_dict[val] - len(val) + 3
            result += f'{space * " "}{val}|'
        result += "\n"
        i = 1
        for row in data:
            space = len(data) // 10 - len(str(i)) + 2
            result += f'{space * " "}{i}|'
            for key, val in row.items():
                space = size_dict[key] - len(val) + 3
                result += f'{space * " "}{val}|'
            result += "\n"
            i += 1

        return result
