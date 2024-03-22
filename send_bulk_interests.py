from api import send_interest
from config import EXPRESSED_INTEREST_FILEPATH
from person import get_username_to_checksum_map

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


username = 'XSTS6527'

if username not in already_sent:
    checksum = get_profile_checksum(username)
    done = send_interest(checksum)
    if done:
        add_to_sent_interests(username)
        already_sent.add(username)