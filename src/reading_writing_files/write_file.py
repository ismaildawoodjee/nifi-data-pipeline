"""Writing to a CSV file"""
import csv


def write_example_csv():

    with open("example.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        header = ["name", "age"]
        writer.writerow(header)

        row = ["Wesley", 26]
        writer.writerow(row)


if __name__ == "__main__":
    write_example_csv()
