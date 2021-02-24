from config import *
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def postAd(data):
    headers = {
        'Host': 'ecg-api.gumtree.com.au',
        'Authorization': Authorization,
        'Accept': '*/*',
        'X-ECG-VER': '1.49',
        'X-ECG-AB-TEST-GROUP': 'GROUP_50;gblandroid_6959_d',
        'Accept-Encoding': 'gzip, deflate',
        'X-ECG-UDID': X_ECG_UDID,
        'X-ECG-Authorization-User': 'id={}, '
                                    'token={}"'.format(accountId, token),
        'Accept-Language': 'en-AU',
        'Content-Length': '104',
        'User-Agent': 'com.ebay.gumtree.au 6.2.0 (Genymotion Google Nexus 5X - 6.0; Android 6.0; en_US)',
        'Connection': 'close',
        'X-ECG-Original-MachineId': machineId,
        'Content-Type': 'application/xml',
    }
    #print headers
    xml = """<delete-ad xmlns="http://www.ebayclassifiedsgroup.com/schema/ad/v1"><reason>NO_REASON</reason></delete-ad>"""
    #print xml
    # url = "https://ecg-api.gumtree.com.au/api/users/{}/ads".format(data)
    #print data
    response = requests.delete(data, headers=headers, data=xml)
    count = 0
    if response.status_code == 204:
        print "[+] Ad Deleted Successfully"
        count = count + 1

    else:
        print "[-] Something went wrong while deleting ad"
        print response.status_code
        #print response.content
        #print response.headers
        print response.url
        count = count - 1
