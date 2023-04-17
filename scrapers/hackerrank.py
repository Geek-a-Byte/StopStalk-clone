import requests
from bs4 import BeautifulSoup as bs
import lxml
import json

from dotenv import load_dotenv
import os

load_dotenv()

# Build the login payload
payload = {
'username': 'geek_a_byte32', #<-- your username
'password': os.getenv("hr_password"), #<-- your password
'remember':'1' 
}

import requests
import argparse
import os
import json
import shutil

from math import ceil
from time import sleep


base_url = "https://www.hackerrank.com/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
login_url = base_url + "auth/login"
submissions_url = base_url + "rest/contests/master/submissions/?offset={}&limit={}"
hackos_url= base_url + "rest/hackers/geek_a_byte32/hackos/?offset={}&limit={}"

username, password = "geek_a_byte32", os.getenv("hr_password")
pages, timeout = 300,10

session = requests.Session()  # log in
logon_response = session.post(
    login_url, auth=(username, password), headers={"user-agent": user_agent}
)
cookies, headers = session.cookies.get_dict(), logon_response.request.headers
logon_json = logon_response.json()  # handle errors

# r = session.get(submissions_url.format(0, 1000), headers=headers)
r2 = session.get(hackos_url.format(0, 1000), headers=headers)

print(r2.status_code)
datum = r2.json()['models']

# print(datum)
number=0
total_count=set();
# Print the parsed data
for data in datum:
  if '/challenges/' in data['link']:
    total_count.add(data['id'])

number=len(total_count)
