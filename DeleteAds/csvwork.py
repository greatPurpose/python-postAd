import csv

# def writeHeader(fileName):
#     myListHeader = []
#     myListHeader.append('address')
#     myListHeader.append('lat')
#     myListHeader.append('long')
#     myListHeader.append('categoryId')
#     myListHeader.append('description')
#     myListHeader.append('contact_email')
#     myListHeader.append('locationId')
#     myListHeader.append('contact_name')
#     myListHeader.append('amount')
#     myListHeader.append('title')
#     myListHeader.append('listOfPics')
#     with open(fileName + '.csv', 'a') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerow(myListHeader)

# writeHeader("products")


def readCsv(fileName):
    productList = []
    with open(fileName + '.txt', 'rU') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        try:
            for row in csv_reader:
                if any(row):
                    line_count += 1
                    adID = row[0]
                    productList.append({"adId": adID})

        except Exception as e:
            print e
    return productList
# print readCsv("products")
