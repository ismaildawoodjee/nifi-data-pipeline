import pandas as pd
from faker import Faker
import csv
import os

filepath = "/home/airflow/sourcefiles/chapter3"


def generate_fake_data():
    fake = Faker()

    with open(
        os.path.join(filepath, "fake_data.csv"),
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

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


def convert_csv_to_json():
    df = pd.read_csv(os.path.join(filepath, "fake_data.csv"))

    for _, row in df.iterrows():
        print(row["name"])

    df.to_json(os.path.join(filepath, "from_airflow.json"), orient="records")
