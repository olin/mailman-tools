"""
A script to upload all archives found in the ./archives folder to gmail,
the username and password are stored as environmental variables, ask either
Cory Dolphin or Tim Cameron Ryan (or whoever else is in charge in the future)
for credentials.
Mailman-downloader is a git submodule and contains generic code written
with the intent of re-use. 

The debug flag is for testing uploads and parsing, instead of deleting the
emails from gmail, simply remove the label, as Gmail's imap labels
are somewhat of a flustercuck, and will duplicate messages willy-nilly.

Please excuse the path hack, it is far simpler than renaming the project

Written by @wcdolphin 2013
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'mailman-downloader'))
from gmail_uploader import uploadToGmail


password = os.environ.get('ARCHIVE_PASS', "Ask Cory or whoever is in charge")
address = os.environ.get('ARCHIVE_LOGIN', "olinlistarchive@gmail.com")

DEBUG = False
root_dir = "archives"


for directory_name in os.listdir(root_dir):
    full_path =  os.path.join(root_dir,directory_name)
    if os.path.isdir(full_path):
        print "Uploading achives for:%s" % directory_name
        if DEBUG:
            print "DEBUG=True, uploading to :list_name:DEBUG"
        directory_name +="DEBUG"
        uploadToGmail(full_path,address,password,directory_name, True)
