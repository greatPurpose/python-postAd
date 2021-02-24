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
    with open(fileName + '.csv', 'rU') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                # print row
                line_count += 1

                categoryName = row[1]
                categoryId = row[0]
                if len(row[2]) > 20:
                    description = row[2]
                else:
                    raise Exception("[-] Description length should be min 20 characters")
                email = row[3]
                contactName = row[4]
                amount = row[5]
                if len(row[6]) > 1:
                    title = row[6]
                else:
                    raise Exception("[-] Title length should be min 8 characters")
                location = row[7]
                listOfPics = row[8]

                productList.append({"categoryId" : categoryId, "categoryName" : categoryName, "description": description,
                 "contactEmail": email, "contactName" : contactName, "amount": amount, "title": title, "location": location, "listOfPics": listOfPics})
    return productList



# print readCsv("products")
