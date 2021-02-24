import requests

headers = {
    'User-Agent': 'com.ebay.gumtree.au 6.2.0 (Genymotion Google Nexus 5X - 6.0; Android 6.0; en_US)',
    'Accept-Language': 'en-AU',
    'X-ECG-UDID': '57614fb9-7c95-409e-985c-8f39530f6fb7',
    'Connection': 'close',
    'Pragma': 'no-cache',
    'X-ECG-Platform': 'android',
    'X-ECG-App-Version': '6.2.0',
    'X-ECG-AB-TEST-GROUP': 'GROUP_50;gblandroid_6959_d',
    'Authorization': 'Basic YXVfYW5kcm9pZF9hcHBfMjA6ZWNnYXBpZ3VtdHJlZWF1',
    'X-ECG-Authorization-User': 'id=\\"1404996592471\\", token=\\"a6c9600e805f65bc8c1a5b731f6905a0d36f3e09b79f593553376935538a57a7\\"',
    'X-ECG-Original-MachineId': '79R6pFoCXWwyurEAwM0xH38ADhJ83-1H49POrP-BMcYkedB91DdWgy9FoBj_TXQV7lnND_9gn9zJVxmrcwwLJSJ4K0eP41ZsyiLYFriXE_g',
    'Host': 'ecg-api.gumtree.com.au',
    'Accept-Encoding': 'gzip, deflate',
}

response = requests.get('https://ecg-api.gumtree.com.au/api/papi/draftAd', headers=headers, verify=False)
