"""
A script to download all mailman list archives for Olin's mailing lists,
the username and password are stored as environmental variables, ask either
Cory Dolphin or Tim Cameron Ryan (or whoever else is in charge in the future)
for credentials.
Mailman-downloader is a git submodule and contains generic code written
with the intent of re-use. 

Please excuse the path hack, it is far simpler than renaming the project

Written by @wcdolphin 2013
"""


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'mailman-downloader'))

from mailman_downloader import download
if __name__ == '__main__':

    download(['https://lists.olin.edu/mailman/private/carpediem/',
              'https://lists.olin.edu/mailman/private/helpme/',
              'https://lists.olin.edu/mailman/private/randomness/'],
        password=os.environ.get('ARCHIVE_PASS', "olinlistarchive@gmail.com"),
        username=os.environ.get('ARCHIVE_LOGIN', "OlinHasNoTrees"),
        force=True,
        dest='./archives'
    )
