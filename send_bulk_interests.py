import time

from api import send_interest
from config import EXPRESSED_INTEREST_FILEPATH, CURR_WORKING_PATH
from utils import get_username_to_checksum_map, read_all_usernames_from_folder

username_checksum_map = get_username_to_checksum_map()

def load_already_sent():
    usernames = set()
    with open(EXPRESSED_INTEREST_FILEPATH, "r") as file:
        for line in file:
            uname = line.strip()
            usernames.add(uname)
    return usernames

def get_profile_checksum(username):
    if username in username_checksum_map:
        return username_checksum_map.get(username)

    print(f'checksum for {username} does not exist')
    return username

def add_to_sent_interests(username):
    with open(EXPRESSED_INTEREST_FILEPATH, "a") as file:
        file.write(f"{username}\n")


already_sent = load_already_sent()
for idx, username in enumerate(read_all_usernames_from_folder(CURR_WORKING_PATH)):
    if username not in already_sent:
        checksum = get_profile_checksum(username)
        done, err = send_interest(checksum)
        time.sleep(1)
        if done:
            print(f'{idx} Interest successfully sent to username {username}')
            add_to_sent_interests(username)
            already_sent.add(username)
        elif err and 'CEB2029' in err:
            print(f'{idx} already sent. username {username} error: {err}')
            add_to_sent_interests(username)
            already_sent.add(username)
        else:
            print(f'{idx} error with username {username} error: {err} msg: {"profile is deleted" if err and "CEB2009" in err else "unknown"}')