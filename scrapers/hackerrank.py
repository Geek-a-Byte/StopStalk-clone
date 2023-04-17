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

#header string picked from chrome
headerString='''
{
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
'''
d = json.loads(headerString)


# Login URL
base_url = "https://www.hackerrank.com/"
login_url = base_url+"/auth/login"
hackos_url= base_url + "rest/hackers/{}/hackos/?offset={}&limit={}"


#creating session
s = requests.Session()
r = s.get(login_url, headers=d)

username, password = payload['username'], payload['password']
# pages, timeout = 300,10


logon_response = s.post(
    login_url, auth=(username, password), headers=d
)
cookies, headers = s.cookies.get_dict(), logon_response.request.headers

r2 = s.get(hackos_url.format(username,0, 1000), headers=headers)
print(r2.status_code)
datum = r2.json()
datum = datum['models']
# print(datum)
number=0
total_count=set();
# Print the parsed data
for data in datum:
  if '/challenges/' in data['link']:
    total_count.add(data['id'])

number=len(total_count)
print(number)



url2=f"https://www.hackerrank.com/rest/hackers/{payload['username']}/badges"


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

