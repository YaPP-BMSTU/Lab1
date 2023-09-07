from csv import *
from metrics import *


def main():
    filename = str(input("Enter file path: "))

    csv = CSV(filename)
    data = csv.parse_csv()

    if len(data) == 0:
        exit(-1)

    while True:
        region = str(input("Enter region: "))
        col = str(input("Enter column number: "))

        if len(region) == 0 or len(filename) == 0:
            print("Error, input field is empty")
            continue
        if not col.isdigit():
            print("Error, column must be a number")
            continue

        metric = Metrics(data, region, col)
        print(metric)
        print(f'min:{metric.min()}, max:{metric.max()}, median:{metric.median()}, average:{metric.average()}')


if __name__ == '__main__':
    main()
