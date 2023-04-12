from flask import Flask, render_template
import cses_scraper as cses_sc
import loj_scraper as loj_sc
import leetcode_scraper as lc_sc
import hr_scraper as hr_sc
import cf_scraper as cf_sc
import toph_scraper as tp_sc
import spoj_scraper as sp_sc
import uva_scraper as uva_sc

app = Flask(__name__)

oj = ['cses', 'loj', 'leetcode','hackerrank','codeforces','toph', 'spoj','uva']
oj_index=[1,2,3,4,5,6,7,8]
solved =[cses_sc.cses,
         loj_sc.loj, 
         lc_sc.leetcode, 
         hr_sc.total_count, 
         cf_sc.cf, 
         tp_sc.toph,
         sp_sc.spoj,
         uva_sc.uva
         ]
usernames =[cses_sc.cses_username, 
            loj_sc.loj_username, 
            lc_sc.lc_user, 
            hr_sc.payload['username'], 
            cf_sc.user,
            tp_sc.username,
            sp_sc.username,
            uva_sc.username,
            ]
urls = [cses_sc.cses_url, 
        loj_sc.loj_url, 
        'https://leetcode.com/'+lc_sc.lc_user,
        'https://www.hackerrank.com/'+hr_sc.payload['username'],
        'https://codeforces.com/profile/'+cf_sc.user,
        'https://toph.co/u/'+tp_sc.username,
        'https://www.spoj.com/users/'+sp_sc.username,
        uva_sc.profile_url, 
        ]

tot_all=0
for i in solved:
    tot_all+=int(i)
    

@app.route('/')
def index():
    return render_template('index.html',   oj_count_username_url=zip(oj_index, oj, solved, usernames,urls), tot_all=tot_all)

# main driver function
if __name__ == '__main__': 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()