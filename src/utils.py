import json
import os


def loadtrfrom_json():
    file_path = "C:\\Users\\Dmitriy\\PycharmProjects\\pyProject\\data\\operations.json"  # os.path.join('data', 'operations.json')
    if not os.path.isfile(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().strip()

    if not content:
        return []

    try:
        data = json.loads(content)

        if isinstance(data, list):
            return data
        else:
            return []
    except json.JSONDecodeError:
        return []


data = print(loadtrfrom_json())
