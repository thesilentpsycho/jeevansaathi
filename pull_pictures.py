import json
import os
import time

from api import get_pics
from config import PROFILES_DATA_PATH, PICS_DATA_PATH, DELAY_IS_SECONDS
from person import Person, load_people


def dump(pdata):
    pics_data_json = json.dumps(pdata, indent=2)
    with open(PICS_DATA_PATH, 'w') as json_file:
        json_file.write(pics_data_json)


pics_data = {}
if os.path.exists(PICS_DATA_PATH):
    with open(PICS_DATA_PATH, 'r') as json_file:
        pics_data = json.load(json_file)

i = 1
for person_data in load_people():
    person = Person(**person_data.__dict__)
    print("Serial: ", i)
    if person.checksum not in pics_data.keys():
        pics = get_pics(person.checksum)
        pics_data[person.checksum] = pics
        if i % 10 == 0:
            dump(pics_data)
        time.sleep(DELAY_IS_SECONDS)
    i += 1

