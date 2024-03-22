import json
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import ALL_PICS_DATA_FILE, DATA_PATH
from person import person_decoder


def load_all_usernames_in_dir(directory_name):
    result = set()
    if os.path.exists(directory_name):
        for filename in os.listdir(directory_name):
            if filename.endswith('.jpg'):
                username = os.path.splitext(filename)[0]
                result.add(username)
    return result


def dump_pics_cdn_links_data(pdata):
    pics_data_json = json.dumps(pdata, indent=2)
    with open(ALL_PICS_DATA_FILE, 'w') as json_file:
        json_file.write(pics_data_json)


def load_pics_cdn_links_data():
    if os.path.exists(ALL_PICS_DATA_FILE):
        with open(ALL_PICS_DATA_FILE, 'r') as json_file:
            return json.load(json_file)
    else:
        return {}


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


def download_image(idx, link, file_name, already_downloaded, output_folder):
    if file_name in already_downloaded:
        return
    if link is None or link == 'None':
        return

    response = requests.get(link)

    if response.status_code == 200:
        full_path = os.path.join(output_folder, file_name)

        with open(full_path, 'wb') as file:
            file.write(response.content)
        print(f"Serial: {idx} Saved '{file_name}'")
    else:
        print(f"Failed to download '{file_name}'. Status code: {response.status_code}")


def download_images_parallel(image_links, already_downloaded, output_folder, max_workers=10):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(download_image, idx, img_link, filename, already_downloaded, output_folder) for idx, (filename, img_link) in enumerate(image_links.items())]

        for future in as_completed(futures):
            future.result()
