from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
import pandas as pd

username = "77547"
url = f"https://cses.fi/user/{username}/"

# Make a GET request to the user's profile page
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to fetch data from the CSES API")
    exit()


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find_all('table')
df1 = pd.read_html(str(table))[1]
df2 = pd.read_html(str(table))[2]
print(df1)
print(df2)

df = pd.DataFrame(df1)
cses = df.iloc[0]['solved tasks']



import requests
from bs4 import BeautifulSoup
import pandas as pd

username = "geek-a-byte"
url = f"https://lightoj.com/user/{username}/"

# Make a GET request to the user's profile page
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to fetch data from the CSES API")
    exit()


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

span1, span2 = soup.find("div", {"class": "like-count mr-4"}).find_all('span')

# Check if the div element was found

if span1 is not None:
    # Extract the number of solved problems from the div text
    loj = span1.text.strip()
    print(f"{username} has solved {loj} problems on LightOJ")
else:
    print("Could not find the number of solved problems on the user's profile page")



import pandas as pd
import requests
import json

user = "nazia32"
api_endpoint = f"https://leetcode.com/graphql"

def extract_json(dict):
  user=dict['user']
  opName=dict['opName']
  Query=dict['Query']
  data={
  "operationName": opName,
  "variables": {"username":user},
  "query": Query
  }
  header={
      "Referer":f"https://leetcode.com/{user}",
      'Content-type':'application/json'
  
  }
  s=requests.session()
  s.get("https://leetcode.com/")
  header["x-csrftoken"] = s.cookies["csrftoken"]
  r = s.post("https://leetcode.com/graphql",json=data,headers=header)
  return json.loads(r.text)

query = '''
query skillStats($username: String!) {
    matchedUser(username: $username) {
    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
      tagProblemCounts {
        advanced {
          tagName
          problemsSolved
        }
        intermediate {
          tagName
          problemsSolved
        }
        fundamental {
          tagName
          problemsSolved
        }
      }
    }
  }
'''
json_data1=extract_json({"user":user,"opName":"skillStats","Query":query})

try:
  df_data1 = json_data1['data']['matchedUser']['tagProblemCounts']['intermediate']
  df_data2=json_data1['data']['matchedUser']['tagProblemCounts']['fundamental']
  df_data3=json_data1['data']['matchedUser']['tagProblemCounts']['advanced']
  df_data4=json_data1['data']['matchedUser']['submitStats']['acSubmissionNum']
  df_intermediate= pd.DataFrame(df_data1)
  df_fundamental= pd.DataFrame(df_data2)
  df_advanced= pd.DataFrame(df_data3)
  df_total = pd.DataFrame(df_data4)
  leetcode = df_total.iloc[0]['count']
  print(df_intermediate)
  print(df_advanced)
  print(df_fundamental)
  print(df_total)
  print(leetcode)
except:
  print("The user does not exist!")

@app.route('/')
def index():
    return render_template('index.html', solved_count={'cses':cses,'loj':loj, 'leetcode':leetcode})

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()