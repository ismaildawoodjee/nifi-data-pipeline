import json


def read_json_file():
    with open("fake_data.json", "r") as file:
        data = json.load(file)

    return data["records"][0]["name"]


if __name__ == "__main__":
    read_json_file()
