import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from config import *
import xml.etree.ElementTree as ET


def postAd(data):

    headers = {
        'User-Agent': 'Gumtree 12.0.0 (iPhone; iOS 12.2; en_AU)',
        'Accept-Language': 'en-AU',
        'X-ECG-VER': '1.51',
        'X-ECG-UDID': X_ECG_UDID,
        'Accept': 'application/xml',
        'Connection': 'close',
        'Pragma': 'no-cache',
        'X-ECG-AB-TEST-GROUP': 'GROUP_50;gblandroid_6959_d',
        'Authorization': Authorization,
        'X-ECG-Authorization-User': 'id={}, '
                                    'token={}"'.format(accountId, token),
        'X-ECG-Original-MachineId': machineId,
        'X-THREATMETRIX-SESSION-ID': sessionId,
        'Content-Type': 'application/xml; charset=UTF-8',
        'Host': 'ecg-api.gumtree.com.au',
        'Accept-Encoding': 'gzip, deflate',
    }
    url = "https://ecg-api.gumtree.com.au/api/users/{}/ads".format(email)
    response = requests.post(url, headers=headers, data=data, verify=False)
    if response.status_code == 201:
        #print data
        print "[+] Ad Posted Successfully"
        # print response.content
        tree = ET.ElementTree(ET.fromstring(response.content))
        root = tree.getroot()

        for child in root:
            if "rel" in child.attrib:
                if child.attrib["rel"] == "self":
                    print "AdId: {}".format(child.attrib["href"])

    else:
        print "[-] Something went wrong while posting ad"
        print response.status_code
        print response.content
