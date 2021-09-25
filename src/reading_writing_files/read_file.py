"""Reading a CSV file"""
import csv


def read_fake_data():
    with open("fake_data.csv") as file:
        # DictReader allows calling by row name, e.g. row['name], instead of row index
        reader = csv.DictReader(file)

        header = next(reader)
        for row in reader:
            print(row["name"])


if __name__ == "__main__":
    read_fake_data()
