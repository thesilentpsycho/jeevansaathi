import requests

cookies = {
    'JS_MOBILE': 'N',
    'JS_TABLET_MOBILE': 'N',
    'pagesABTestingTrackingv1': '%7B%22autoId%22%3A%22306041708747805%22%2C%22flow%22%3A%22A%22%7D',
    '_gcl_au': '1.1.480761598.1708747806',
    '__utmz': '196881587.1708747806.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '_fbp': 'fb.1.1708747806233.1767115888',
    'remnam': 'VUVU3605',
    'rempas': 'BPZieO8WKgGbYNJiE3Jvd6IABdPRgC%2FG',
    'loginTracking': '%5B%22VUVU3605%22%5D',
    '_jsdid': 'CcXijEw-chktdFeMacIntelGoogle_PC',
    'test_js': 'y',
    '__utma': '196881587.653839176.1708747806.1708747806.1708907030.2',
    'chatEncrypt': '8009063e5ac88cd33a08fc887046594e',
    '_ga': 'GA1.1.653839176.1708747806',
    '_clck': 'qktcc6%7C2%7Cfk9%7C0%7C1515',
    '_ga_H73EBTE0B2': 'GS1.1.1710993452.37.1.1710996576.0.0.0',
    '_clsk': 'toufb1%7C1710998329224%7C128%7C0%7Ce.clarity.ms%2Fcollect',
    'AUTHCHECKSUM': 'eyJhbGciOiJIUzI1NiJ9.eyJ2ZXIiOjIuMCwicGlkIjo1NDIwNjk4MywidG9rZW4iOiJERDVERHNHa0REUkNqc2thMkM4QzE1YjEzczM4RDZEayIsImF0IjoxNzExMDAxNzY3LCJhcCI6e319.wAoZr9k5snr1RB81TU6Homcb35reacUtnwlwRgme3NE',
    '_ga_8HM2HLDNVF': 'GS1.1.1711001770.43.1.1711001822.0.0.0',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'JS_MOBILE=N; JS_TABLET_MOBILE=N; pagesABTestingTrackingv1=%7B%22autoId%22%3A%22306041708747805%22%2C%22flow%22%3A%22A%22%7D; _gcl_au=1.1.480761598.1708747806; __utmz=196881587.1708747806.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1708747806233.1767115888; remnam=VUVU3605; rempas=BPZieO8WKgGbYNJiE3Jvd6IABdPRgC%2FG; loginTracking=%5B%22VUVU3605%22%5D; _jsdid=CcXijEw-chktdFeMacIntelGoogle_PC; test_js=y; __utma=196881587.653839176.1708747806.1708747806.1708907030.2; chatEncrypt=8009063e5ac88cd33a08fc887046594e; _ga=GA1.1.653839176.1708747806; _clck=qktcc6%7C2%7Cfk9%7C0%7C1515; _ga_H73EBTE0B2=GS1.1.1710993452.37.1.1710996576.0.0.0; _clsk=toufb1%7C1710998329224%7C128%7C0%7Ce.clarity.ms%2Fcollect; AUTHCHECKSUM=eyJhbGciOiJIUzI1NiJ9.eyJ2ZXIiOjIuMCwicGlkIjo1NDIwNjk4MywidG9rZW4iOiJERDVERHNHa0REUkNqc2thMkM4QzE1YjEzczM4RDZEayIsImF0IjoxNzExMDAxNzY3LCJhcCI6e319.wAoZr9k5snr1RB81TU6Homcb35reacUtnwlwRgme3NE; _ga_8HM2HLDNVF=GS1.1.1711001770.43.1.1711001822.0.0.0',
    'DNT': '1',
    'JB-Profile-Identifier': 'eyJhbGciOiJIUzI1NiJ9.eyJ2ZXIiOjIuMCwicGlkIjo1NDIwNjk4MywidG9rZW4iOiJERDVERHNHa0REUkNqc2thMkM4QzE1YjEzczM4RDZEayIsImF0IjoxNzExMDAxNzY3LCJhcCI6e319.wAoZr9k5snr1RB81TU6Homcb35reacUtnwlwRgme3NE',
    'JS-Profile-Identifier': 'eyJhbGciOiJIUzI1NiJ9.eyJ2ZXIiOjIuMCwicGlkIjo1NDIwNjk4MywidG9rZW4iOiJERDVERHNHa0REUkNqc2thMkM4QzE1YjEzczM4RDZEayIsImF0IjoxNzExMDAxNzY3LCJhcCI6e319.wAoZr9k5snr1RB81TU6Homcb35reacUtnwlwRgme3NE',
    'JS-User-Agent': 'JSPC',
    'Origin': 'https://www.jeevansathi.com',
    'Referer': 'https://www.jeevansathi.com/profile-detail/3af2a219593f225d1f05bbfc54f3deeci58834813?stype=4',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = {
    'profileCheckSum': '3af2a219593f225d1f05bbfc54f3deeci58834813',
}

response = requests.post(
    'https://www.jeevansathi.com/app-gateway/jscontact/v1/bookmarks',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"profileCheckSum":"3af2a219593f225d1f05bbfc54f3deeci58834813"}'
#response = requests.post(
#    'https://www.jeevansathi.com/app-gateway/jscontact/v1/bookmarks',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)