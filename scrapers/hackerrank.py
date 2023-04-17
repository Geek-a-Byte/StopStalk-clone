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
from bs4 import BeautifulSoup as bs
import lxml
import json

#header string picked from chrome
headerString='''
{
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
'''
d = json.loads(headerString)


# Login URL
login_url = 'https://www.hackerrank.com/auth/login'

#creating session
s = requests.Session()
r = s.get(login_url, headers=d)

# Get the csrf-token from meta tag
soup = bs(r.text,'lxml')
# csrf_token = soup.select_one('meta[name="csrf-token"]')['content']

# # Page header
# head = { 
#     'Content-Type':'application/x-www-form-urlencoded',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
# }

# # Set CSRF-Token
# head['X-CSRF-Token'] = csrf_token
# head['X-Requested-With'] = 'XMLHttpRequest'


# Get the page cookie
cookie = r.cookies


# Build the login payload
payload = {
'username': 'geek_a_byte32', #<-- your username
'password': os.environ.get('hr_password'), #<-- your password
'remember':'1' 
}

# # Try to login to the page
r = s.post(login_url, cookies=cookie, data=payload, headers=d)
# soup = bs(r.text,'lxml')
# print(soup)
print(r.text)


url2='https://www.hackerrank.com/rest/hackers/geek_a_byte32/badges'


# Try to get a page behind the login page
r = s.get(url2, headers=d)

print(r.status_code)

# # Check if login was successful, if so there have to be an element with the id menu_row2
soup = bs(r.text, 'lxml')

# Parse the response JSON
datum = r.json()['models']

total_count=0;
# Print the parsed data
for data in datum:
    print(data['badge_name'],end=' ')
    print(data['solved'])
    total_count+=data['solved']
print(total_count)