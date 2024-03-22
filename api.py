import requests
import json

from config import AUTH_TOKEN

def send_interest(profile_checksum):
    url = "https://www.jeevansathi.com/app-gateway/jscontact/v1/initiate"

    payload = json.dumps({
        "profileCheckSum": "{}".format(profile_checksum),
        "pageSource": "VDP",
        "searchType": "4"
    })
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': 'AUTHCHECKSUM={}'.format(AUTH_TOKEN),
        'DNT': '1',
        'JB-Profile-Identifier': AUTH_TOKEN,
        'JS-Profile-Identifier': AUTH_TOKEN,
        'JS-User-Agent': 'JSPC',
        'Origin': 'https://www.jeevansathi.com',
        'Referer': f'https://www.jeevansathi.com/profile-detail/{profile_checksum}?stype=4',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return True

    return False


def get_pics(profile_checksum):

    url = f"https://api.jeevansathi.com/jsprofile/v2/profiles?rtype=json&ids={profile_checksum}&vt=media"

    payload = {}
    headers = {
      'Accept': 'application/json',
      'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
      'Connection': 'keep-alive',
      'DNT': '1',
      'JB-Profile-Identifier': AUTH_TOKEN,
      'JS-Profile-Identifier': AUTH_TOKEN,
      'JS-User-Agent': 'JSPC',
      'Origin': 'https://www.jeevansathi.com',
      'Referer': 'https://www.jeevansathi.com/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
      'X-Requested-With': 'XMLHttpRequest',
      'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'Cookie': 'AUTHCHECKSUM={}'.format(AUTH_TOKEN)
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resp_json = json.loads(response.text)
    pics = []
    try:
        pics = [item['originalPicUrl'] for item in resp_json['data']['items'][0]['media']['photo']['items']]
    except Exception as e:
        pics = []
        print(f"Error: {e}")
    return pics



def first_search():
    url = "https://api.jeevansathi.com/api/v3/search/perform?searchsrc=srp1&currentPage=1"

    payload = 'json=%7B%22LAGE%22%3A%2225%22%2C%22HAGE%22%3A%2233%22%2C%22LHEIGHT%22%3A%2214%22%2C%22HHEIGHT%22%3A%2220%22%2C%22RELIGION%22%3A%221%2C9%2C4%22%2C%22SECT%22%3A%22%22%2C%22MTONGUE%22%3A%22%22%2C%22LOCATION%22%3A%2251%22%2C%22LOCATION_CITIES%22%3A%22JH%22%2C%22RES_STATUS%22%3A%22%22%2C%22MSTATUS%22%3A%22N%22%2C%22LINCOME%22%3A%220%22%2C%22HINCOME%22%3A%2219%22%2C%22EDUCATION%22%3A%22%22%2C%22EMPLOYED_IN%22%3A%22%22%2C%22OCCUPATION%22%3A%22%22%2C%22MANGLIK%22%3A%22%22%2C%22GENDER%22%3A%22F%22%2C%22CASTE%22%3A%22%22%2C%22PHOTO%22%3A%22Y%22%2C%22CASTE_GROUP_ID%22%3A%22%22%2C%22SUBCASTE%22%3A%22%22%2C%22DIET%22%3A%22%22%2C%22HAVECHILD%22%3A%22N%22%7D&searchBasedParam=QuickSearchBand'
    headers = {
      'Accept': 'application/json',
      'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
      'Connection': 'keep-alive',
      'Content-Type': 'application/x-www-form-urlencoded',
      'DNT': '1',
      'JB-Profile-Identifier': AUTH_TOKEN,
      'JS-Profile-Identifier': AUTH_TOKEN,
      'JS-User-Agent': 'JSPC',
      'Origin': 'https://www.jeevansathi.com',
      'Referer': 'https://www.jeevansathi.com/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
      'X-Requested-With': 'XMLHttpRequest',
      'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'Cookie': 'AUTHCHECKSUM={}'.format(AUTH_TOKEN)
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def continue_search(search_id, page_num):
    url = f"https://api.jeevansathi.com/api/v3/search/perform?searchsrc=srp1&currentPage={page_num}"

    payload = f'searchId={search_id}&searchBasedParam=QuickSearchBand'
    headers = {
      'Accept': 'application/json',
      'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
      'Connection': 'keep-alive',
      'Content-Type': 'application/x-www-form-urlencoded',
      'DNT': '1',
      'JB-Profile-Identifier': AUTH_TOKEN,
      'JS-Profile-Identifier': AUTH_TOKEN,
      'JS-User-Agent': 'JSPC',
      'Origin': 'https://www.jeevansathi.com',
      'Referer': 'https://www.jeevansathi.com/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
      'X-Requested-With': 'XMLHttpRequest',
      'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'Cookie': 'AUTHCHECKSUM={}'.format(AUTH_TOKEN)
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response

