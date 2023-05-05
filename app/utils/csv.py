import csv


def extract_rncs_from_csv(path):
    rnc_list = []

    with open(path, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        header = next(datareader)
        if header != None:
            for row in datareader:
                print(row)
                rnc_list.append(row)

    return rnc_list
