import csv


def get_csv(filename):
    rows = []
    data_file = open(filename, "r")

    reader = csv.reader(data_file)

    next(reader)
    for row in reader:
        rows.append(row)
    return rows
