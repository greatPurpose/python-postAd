import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from requests_toolbelt.multipart.encoder import MultipartEncoder
import xml.etree.ElementTree as ET
from config import *


def uploadPic(picPath):

    multipart_data = MultipartEncoder(
        fields={
            "file": (
                "adUploadImage.jpg",
                open(picPath, 'rb'),
                "image/jpg"
            )
        }
    )
    headers = {
        'User-Agent': 'com.ebay.gumtree.au 6.2.0 (Genymotion Google Nexus 5X - 6.0; Android 6.0; en_US)',
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
        'Content-Type': multipart_data.content_type,
        'Host': 'ecg-api.gumtree.com.au',
        'Accept-Encoding': 'gzip, deflate',
    }

    try:
        response = requests.post('https://ecg-api.gumtree.com.au/api/pictures', headers=headers, data=multipart_data, verify=False)
        print response.status_code
        # print response.content
        if response.status_code == 201:

            tree = ET.ElementTree(ET.fromstring(response.content))
            root = tree.getroot()

            mList = []
            thumbnail = ""
            normal = ""
            large = ""
            extraLarge = ""
            extraExtraLarge = ""

            for child in root:
                # print(child.attrib)
                if child.attrib["rel"] == "thumbnail":
                    thumbnail = child.attrib["href"]
                elif child.attrib["rel"] == "normal":
                    normal = child.attrib["href"]
                elif child.attrib["rel"] == "large":
                    large = child.attrib["href"]
                elif child.attrib["rel"] == "extraLarge":
                    extraLarge = child.attrib["href"]
                elif child.attrib["rel"] == "extraExtraLarge":
                    extraExtraLarge = child.attrib["href"]

            finalXML = """
            <pic:picture>
                <pic:link href="{}" rel="extraExtraLarge"/>
                <pic:link href="{}" rel="normal"/>
                <pic:link href="{}" rel="thumbnail"/>
                <pic:link href="{}" rel="extraLarge"/>
                <pic:link href="{}" rel="large"/>
            </pic:picture>""".format(extraExtraLarge, normal, thumbnail, extraLarge, large)

            return finalXML

        else:
            return None
    except Exception as e:
        print e

# print uploadPic("images/cat1.png")
