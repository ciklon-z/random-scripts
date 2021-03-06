import re
import requests
import argparse

parser =argparse.ArgumentParser(description='Checking parameters')
parser.add_argument('URL',metavar='U',help='Target')
parser.add_argument('content',metavar='C',help='Textcheck')
param=parser.parse_args()

# set header
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
# set header

try:
    request = requests.get(param.URL, verify=False, headers=hdr)
    geturl_readable = request.text
    word = re.findall(param.content, geturl_readable)

    print word[0]
except:
    raise
