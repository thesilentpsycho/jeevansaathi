import json
import os

from config import PROFILES_DATA_PATH, DATA_PATH


class Person:
    def __init__(self, checksum, username, caste, height, name, age, dp, datadump):
        self.dp = dp
        self.caste = caste
        self.username = username
        self.checksum = checksum
        self.name = name
        self.age = age
        self.height = height
        self.datadump = datadump

    def __str__(self):
        return f"UserName: {self.username}, Profile: {self.checksum}, Name: {self.name}, Age: {self.age}, Caste: {self.caste}, Height: {self.height}"

def person_decoder(obj):
    if 'name' in obj and 'age' in obj and 'height' in obj and 'checksum' in obj and 'username' in obj:
        return Person(obj['checksum'], obj['username'], obj['caste'], obj['height'], obj['name'], obj['age'], obj['dp'], None)
    return None

def load_people():
    if os.path.exists(PROFILES_DATA_PATH):
        with open(PROFILES_DATA_PATH, 'r') as json_file:
            loaded_json_data = json.load(json_file, object_hook=person_decoder)
            return loaded_json_data
    else:
        return []


def load_all_people_data():
    result = []
    if os.path.exists(DATA_PATH):
        for filename in os.listdir(DATA_PATH):
            if filename.endswith('.json'):
                file_path = os.path.join(DATA_PATH, filename)
                with open(file_path, 'r') as json_file:
                    loaded_json_data = json.load(json_file, object_hook=person_decoder)
                    result.extend(loaded_json_data)
    return result


def get_username_to_checksum_map():
    people = load_all_people_data()
    result = {}
    for curr in people:
        if curr is not None and curr.username and curr.checksum:
            result[curr.username] = curr.checksum
    return result

class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age, "height": obj.height, "dp": obj.dp,
                    "username": obj.username, "checksum": obj.checksum, "caste": obj.caste, "datadump": obj.datadump}
        return super().default(obj)


def dump_people(people):
    people_data = json.dumps(people, cls=PersonEncoder, indent=2)
    json_file_path = PROFILES_DATA_PATH
    with open(json_file_path, 'w') as json_file:
        json_file.write(people_data)
    print(f"JSON file '{json_file_path}' created successfully.")
