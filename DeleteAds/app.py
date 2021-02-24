from csvwork import readCsv
from postad import postAd
from config import accountId
from config import csvLocation

import time

print("start")
listOfProducts = readCsv(csvLocation)

for product in listOfProducts:
    print product
    adId = product["adId"]
    data = """https://ecg-api.gumtree.com.au/api/users/{}/ads/{}""".format(accountId, adId)
    # print data
    time.sleep(1)
    try:
        postAd(data)
        # print data
    except ConnectionError as e:
        print e
        print data
