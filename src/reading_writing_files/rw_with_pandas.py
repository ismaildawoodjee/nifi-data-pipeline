import pandas as pd


def write_to_csv():

    df = pd.read_csv("fake_data.csv")

    data = {
        "Name": ["Elizabeth", "Aaron", "Emily", "Wanda"],
        "Age": [65, 32, 53, 78],
    }

    example_df = pd.DataFrame(data)

    example_df.to_csv("example_df.csv", index=False)


if __name__ == "__main__":
    write_to_csv()
