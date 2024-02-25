import json
import requests
import time

from api import continue_search
from config import PROFILES_DATA_PATH, SEARCH_ID, NUM_OF_RESULTS, AUTH_TOKEN, DELAY_IS_SECONDS
from person import Person, load_people, dump_people

auth_token = AUTH_TOKEN
delay_seconds = DELAY_IS_SECONDS


search_id = SEARCH_ID
no_of_results = NUM_OF_RESULTS

people = load_people()
for curr_page in range(1, int(no_of_results/20) + 1):
    time.sleep(delay_seconds)
    print('Page Number: ', curr_page)
    resp = continue_search(search_id, curr_page)
    resp_json = json.loads(resp.text)
    for profile in resp_json['profiles']:
        checksum = profile['profilechecksum']
        username = profile['username']
        caste = profile['caste']
        height = profile['height']
        name = profile['name_of_user']
        age = profile['age']
        try:
            dp = profile['photo']['url']
        except:
            dp = None
        people.append(Person(checksum, username, caste, height, name, age, dp))
    if curr_page % 5 == 0:
        dump_people(people)
