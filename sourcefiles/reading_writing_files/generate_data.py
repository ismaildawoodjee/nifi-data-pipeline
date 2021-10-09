"""Generate fake data using the Faker library"""
from faker import Faker
import csv


def generate_fake_data():
    fake = Faker()

    with open("fake_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        header = ["name", "age", "street", "city", "state", "zip", "lng", "lat"]
        writer.writerow(header)

        for _ in range(1000):
            writer.writerow(
                [
                    fake.name(),
                    fake.random_int(min=18, max=80, step=1),
                    fake.street_address(),
                    fake.city(),
                    fake.state(),
                    fake.zipcode(),
                    fake.longitude(),
                    fake.latitude(),
                ]
            )


if __name__ == "__main__":
    generate_fake_data()
