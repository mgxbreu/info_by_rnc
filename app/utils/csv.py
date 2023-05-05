import csv


def extract_rncs_from_csv(path):
    rnc_list = []

    with open(path, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        header = next(datareader)
        if header != None:
            for row in datareader:
                rnc_list.append(row)

    return rnc_list


def write_row(row, headers):
    with open('data.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=headers)

        if f.tell() == 0:
            writer.writeheader()

        writer.writerow(row)
