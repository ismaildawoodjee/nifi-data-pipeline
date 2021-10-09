"""Generate fake data and output it as JSON"""
from faker import Faker
import json


def generate_fake_json_data():
    fake = Faker()

    with open("fake_data.json", "w", encoding="utf-8") as file:
        # A dictionary...
        data = {}
        # containing a list...
        data["records"] = []

        for _ in range(1000):
            row = {
                "name": fake.name(),
                "age": fake.random_int(min=18, max=80, step=1),
                "street": fake.street_address(),
                "city": fake.city(),
                "state": fake.state(),
                "zip": fake.zipcode(),
                "lng": float(fake.longitude()),
                "lat": float(fake.latitude()),
            }
            # of dictionaries.
            data["records"].append(row)
        # dump data into the JSON file
        json.dump(data, file)


if __name__ == "__main__":
    generate_fake_json_data()
