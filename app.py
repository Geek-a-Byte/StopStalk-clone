from flask import Flask, render_template
import cses_scraper as cses_sc
import loj_scraper as loj_sc
import leetcode_scraper as lc_sc
import hr_scraper as hr_sc

app = Flask(__name__)

oj = ['cses', 'loj', 'leetcode','hackerrank']
solved =[cses_sc.cses,loj_sc.loj, lc_sc.leetcode, hr_sc.total_count]
usernames =[cses_sc.cses_username, loj_sc.loj_username, lc_sc.lc_user, hr_sc.payload['username']]
urls = [cses_sc.cses_url, 
        loj_sc.loj_url, 
        'https://leetcode.com/'+lc_sc.lc_user,
        'https://www.hackerrank.com/'+hr_sc.payload['username']
        ]

tot_all=0
for i in solved:
    tot_all+=int(i)
    

@app.route('/')
def index():
    return render_template('index.html',   oj_count_username_url=zip(oj, solved, usernames,urls), tot_all=tot_all)

# main driver function
if __name__ == '__main__': 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()