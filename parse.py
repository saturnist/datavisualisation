import csv

MY_FILE = "/Users/Saturnist/Google Drive/program/learn_python/dataviz/data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
    opened_file = open(raw_file)

    csv_data = csv.reader(opened_file, delimiter=delimiter)

    parsed_data = []

    fields = next(csv_data)
    # alternatively can use csv_data.__next__()

    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    opened_file.close()

    return parsed_data


def main():
    new_data = parse(MY_FILE, ",")

    print(new_data)


if __name__ == "__main__":
    main()