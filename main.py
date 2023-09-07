from csv import *
from metrics import *


def main():
    while True:
        filename = str(input("Enter file path: "))
        try:
            csv = Csv(filename)
            data = csv.parse_csv()
            if len(data) == 0:
                raise MyException('Error, file is empty')
            break
        except MyException as e:
            print(e.message)
            continue

    table = Table(data)

    while True:
        region = str(input("Enter region: "))
        col = str(input("Enter column number: "))

        if len(region) == 0 or len(filename) == 0:
            print("Error, input field is empty")
            continue
        if not col.isdigit():
            print("Error, column number is invalid")
            continue
        try:
            metric = Metrics(table, region, col)
            print(metric)
            print(f'min:{metric.min()}, max:{metric.max()}, median:{metric.median()}, average:{metric.average()}')
            metric.percentile_table()
        except MyException as e:
            print(e.message)


if __name__ == '__main__':
    main()
