import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from config import DP_OUTPUT_FOLDER
from person import load_people


output_folder = DP_OUTPUT_FOLDER
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

image_links = {f"{person.username}.jpg": f"{person.dp}" for person in load_people()}
already_downloaded = [file for file in os.listdir(output_folder) if os.path.isfile(os.path.join(output_folder, file))]


def download_image(idx, link, file_name):
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


def download_images_parallel(image_links, max_workers=10):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(download_image, idx, img_link, filename) for idx, (filename, img_link) in enumerate(image_links.items())]

        for future in as_completed(futures):
            future.result()


download_images_parallel(image_links, max_workers=10)