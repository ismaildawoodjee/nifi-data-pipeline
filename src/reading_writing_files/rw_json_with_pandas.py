import pandas.io.json as pd_json
import pandas as pd


def read_json_file():
    with open("fake_data.json", "r") as file:
        # load string version of file; the `read` method returns a string
        data = pd_json.loads(file.read())

        # normalize JSON, passing in the key "records"
        df = pd.json_normalize(data, record_path="records")

        # write back to JSON, index-oriented
        # outputs JSON as a dictionary of dictionaries
        df.head(2).to_json("example_json.json")

        # record-oriented (each row is a dictionary/JSON object)
        # outputs JSON as a list of dictionaries
        df.head(2).to_json("example_json_records.json", orient="records")


if __name__ == "__main__":
    read_json_file()
