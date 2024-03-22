import os
import time
import threading
from api import get_pics
from config import CURR_WORKING_PATH, DELAY_IN_SECONDS
from utils import load_all_usernames_in_dir, load_pics_cdn_links_data, dump_pics_cdn_links_data, get_username_to_checksum_map, \
    download_images_parallel


pics_path = os.path.join(CURR_WORKING_PATH, 'multi_pics')
if not os.path.exists(pics_path):
    os.makedirs(pics_path)

pics_data = load_pics_cdn_links_data()
usernames = load_all_usernames_in_dir(CURR_WORKING_PATH)
username_checksum_map = get_username_to_checksum_map()
already_downloaded_pics = {file for file in os.listdir(pics_path) if os.path.isfile(os.path.join(pics_path, file))}


def download_images_async(il, a, p):
    threading.Thread(target=download_images_parallel, args=(il, a, p)).start()


i = 0
for username in usernames:
    if username in pics_data:
        continue

    checksum = username_checksum_map.get(username)
    if checksum:
        pics_links = get_pics(checksum)
        pics_data[username] = pics_links

        i += 1
        print("Serial: ", i)
        if i % 10 == 0:
            dump_pics_cdn_links_data(pics_data)
        image_links = {f"{username}-{idx}.jpg": f"{link}" for idx, link in enumerate(pics_links)}
        download_images_async(image_links, already_downloaded_pics, pics_path)
        time.sleep(DELAY_IN_SECONDS)

