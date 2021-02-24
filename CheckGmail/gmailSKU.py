from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from bs4 import BeautifulSoup
import datetime
import sys

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'c:\\Gumtree\\shopubuy\\CheckGmail\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('c:\\Gumtree\\shopubuy\\CheckGmail\\token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    SkuInput = sys.argv[1]
    
    today = datetime.date.today()
    tomorrow = today - datetime.timedelta(days=1)
    yesterday = today + datetime.timedelta(days=1)
    todayFormatted = today.strftime('%Y/%m/%d')
    yesterdayFormatted = yesterday.strftime('%Y/%m/%d')
    tomorrowFormatted = tomorrow.strftime('%Y/%m/%d')
    
    qParameter = 'subject:'+SkuInput+' has been deleted before:' + yesterdayFormatted + ' after:' + tomorrowFormatted + ' from:noreply@gumtree.com.au'
    #print(qParameter)
    #qParameter = 'from:noreply@gumtree.com.au'
    #qParameter = 'subject:' + SkuInput + ' has been deleted after:2020/4/28 before:2020/4/30 from:noreply@gumtree.com.au'
    results = service.users().messages().list(userId='me', q=qParameter).execute()

    if(results["resultSizeEstimate"] == 0):
        print(None)
    else:
        for msg in results["messages"]:
            payload = service.users().messages().get(userId='me', id=msg["id"], format='full').execute()['payload']
            byteMsg = payload['body']['data']
            text = base64.urlsafe_b64decode(byteMsg.encode('utf-8'))
            soup = BeautifulSoup(text, 'html.parser')
            for i in soup.body.table.findAll('a'):
                id = None
                if (str(i.contents[0]).isdigit()):
                    id = str(i.contents[0])
                    break
            print(str(id))

if __name__ == '__main__':
    main()