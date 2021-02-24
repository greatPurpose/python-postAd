from csvwork import readCsv
from picupload import uploadPic
from postad import postAd
from config import accountId
from config import csvLocation
from requests.exceptions import ConnectionError

listOfProducts = readCsv(csvLocation)

picConcat = ""
for product in listOfProducts:
    # print product

    categoryId = product["categoryId"]
    categoryName = product["categoryName"]
    description = product["description"]
    contactEmail = product["contactEmail"]
    contactName = product["contactName"]
    amount = product["amount"]
    title = product["title"]
    location = product["location"]
    img = product["listOfPics"]
    for pic in product["listOfPics"].split():
        # print img
        print "[+] Uploading Image {}".format(pic.replace(',', '').replace('"', ''))
        picXml = uploadPic(pic.replace(',', '').replace('"', ''))
        print len(picXml)
        if len(picXml) > 400:
            picConcat = picConcat + picXml

    data = """<ad:ad id="" xmlns:ad="http://www.ebayclassifiedsgroup.com/schema/ad/v1" xmlns:cat="http://www.ebayclassifiedsgroup.com/schema/category/v1" xmlns:loc="http://www.ebayclassifiedsgroup.com/schema/location/v1" xmlns:attr="http://www.ebayclassifiedsgroup.com/schema/attribute/v1" xmlns:types="http://www.ebayclassifiedsgroup.com/schema/types/v1" xmlns:pic="http://www.ebayclassifiedsgroup.com/schema/picture/v1" xmlns:vid="http://www.ebayclassifiedsgroup.com/schema/video/v1" xmlns:user="http://www.ebayclassifiedsgroup.com/schema/user/v1" xmlns:feature="http://www.ebayclassifiedsgroup.com/schema/feature/v1">
       <ad:account-id>{}</ad:account-id>
       <ad:adSlots class="java.util.ArrayList"/>
       <ad:ad-address>
          <types:full-address>Sydney NSW, Australia</types:full-address>
          <types:radius>1000</types:radius>
       </ad:ad-address>
       <attr:attributes class="java.util.ArrayList">
          <attr:attribute localized-label="Condition" name="{}.condition" type="ENUM">
             <attr:value>new</attr:value>
          </attr:attribute>
       </attr:attributes>
       <cat:category id="{}"/>
       <ad:description><![CDATA[{}]]></ad:description>
       <ad:email>{}</ad:email>
       <loc:locations class="java.util.ArrayList">
          <loc:location id="{}"/>
       </loc:locations>
       <ad:phone></ad:phone>
       <pic:pictures class="java.util.ArrayList">
          {}
       </pic:pictures>
       <ad:poster-contact-email>{}</ad:poster-contact-email>
       <ad:poster-contact-name>{}</ad:poster-contact-name>
       <ad:price>
          <types:amount>{}</types:amount>
          <types:currency-iso-code>
             <types:value>AUD</types:value>
          </types:currency-iso-code>
          <types:price-type>
             <types:value>SPECIFIED_AMOUNT</types:value>
          </types:price-type>
       </ad:price>
       <ad:title>{}</ad:title>
       <ad:ad-type>
          <ad:value>OFFERED</ad:value>
       </ad:ad-type>
    </ad:ad>""".format(accountId, categoryName, categoryId, description, contactEmail, location, picConcat, contactEmail, contactName, amount, title)


    picConcat = ""
    #print data

    try:
        postAd(data)
    except ConnectionError as e:
        print e
        #print data


