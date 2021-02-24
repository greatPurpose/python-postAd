import imaplib
import email
from argparse import ArgumentParser
import datetime
import re

DEFAULT_IMAP_SERVER = 'imap.gmail.com'
DEFAULT_IMAP_MAIL   = 'iansydney77@gmail.com'
DEFAULT_IMAP_PASS   = 'kil49o123xc'
DEFAULT_SUBJECT     = 'Your ad has been deleted'
LOOKUP_INTERVAL     = 3600 * 1

current_timestamp = (datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds()

# parse CLI arguments
parser = ArgumentParser(add_help=True, description='imap mails parser')
parser.add_argument('-debug', action='store_true', dest='debug', help='Start Selenium in visible mode')
parser.add_argument('-imap_server', action='store', type=str, dest='imap_server',
                    help='Imap server to connect')
parser.add_argument('-mailbox', action='store', type=str, dest='mailbox',
                    help='Mailbox to connect')
parser.add_argument('-password', action='store', type=str, dest='password',
                    help='Mailbox password')
parser.add_argument('-subject', action='store', type=str, dest='subject',
                    help='Subject to search')

args = parser.parse_args()

if args.imap_server is None and args.mailbox is not None:
    args.imap_server = 'imap.' + args.mailbox.split('@')[1]

args.imap_server = DEFAULT_IMAP_SERVER if args.imap_server is None else args.imap_server
args.mailbox = DEFAULT_IMAP_MAIL if args.mailbox is None else args.mailbox
args.password = DEFAULT_IMAP_PASS if args.password is None else args.password
args.subject = DEFAULT_SUBJECT.lower() if args.subject is None else args.subject.lower()
args.subject = re.sub("[^0-9a-zA-Z]+", " ", args.subject).lower()

# connect to server
try:
    svr = imaplib.IMAP4_SSL(args.imap_server)
    svr.login(args.mailbox, args.password)
except Exception as e:
    print(e)
    exit(1)

# cycle through last mails, to find search criteria, or to stop if no matching items in last 3 hours
num = int(svr.select('inbox', readonly=True)[1][0].decode('utf-8'))
start_idx_template = 'of the ad that is currently live on the site:'

while True:
    resp, lst = svr.fetch(num, '(RFC822)')
    body = lst[0][1]
    email_message = email.message_from_string(body)
    mail_timestamp = email.utils.mktime_tz(email.utils.parsedate_tz(email_message['date']))
    subject = re.sub("[^0-9a-zA-Z]+", " ", email_message['subject']).lower()
    num -= 1

    if args.subject in subject:
        # we found mail we want, let's parse it
        if email_message.is_multipart():
            for payload in email_message.get_payload():
                to_parse = payload.get_payload()
                start_idx = to_parse.find(start_idx_template)
                if start_idx != -1:
                    start_idx += len(start_idx_template)
                    end_idx = to_parse[start_idx:].find('</')
                    result = to_parse[start_idx:start_idx + end_idx].strip()
                    length = len(result)
                    id = (result[length - 10:length])
                    print(id)
                    exit(0)
                else:
                    continue
        else:
            to_parse = email_message.get_payload()
            start_idx = to_parse.find(start_idx_template)
            if start_idx != -1:
                start_idx += len(start_idx_template)
                end_idx = to_parse[start_idx:].find('</')
                result = to_parse[start_idx:start_idx + end_idx].strip()
                length = len(result)
                id = (result[length-10:length])
                print(id)
                exit(0)
            else:
                print('-1')
                exit(0)

    if current_timestamp - mail_timestamp > LOOKUP_INTERVAL:
        # mails below is too old, exiting
        print('-2')
        exit(0)

    if num < 0:
        # no more mails in inbox exiting
        print('-3')
        exit(0)
