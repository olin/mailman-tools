import imaplib
import os
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(os.envrion.get('ARCHIVE_LOGIN', "You are so scrood"), os.envrion.get('ARCHIVE_PASS', "You are so scrood"))
print mail.list()

# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.
typ, data = mail.search(None, '(X-GM-RAW "Dust")')
print typ
for numail in data[0].split():
    print numail
    typ, data = mail.fetch(numail, '(RFC822)')
    print 'mailessage %s\n%s\n' % (numail, data[0][1])