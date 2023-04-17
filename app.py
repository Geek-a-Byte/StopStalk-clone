from flask import Flask, render_template
import scrapers
from scrapers import cses, codeforces, hackerrank, leetcode, lightoj, spoj, timus, uva, toph, codechef, atcoder,vjudge
app = Flask(__name__)

oj_index=[1,2,3,4,5,6,7,8,9,10,11,12,13]
oj = ['cses', 'loj', 'leetcode','hackerrank','codeforces','toph', 'spoj','uva','timus','codechef','atcoder', 'vjudge','vjudge']
solved =[
         int(cses.cses),
         int(lightoj.loj), 
         int(leetcode.leetcode), 
         int(hackerrank.total_count), 
         int(codeforces.cf), 
         int(toph.toph),
         int(spoj.spoj),
         int(uva.uva),
         int(timus.number),
         int(codechef.number),
         int(atcoder.number),
         int(vjudge.number1),
         int(vjudge.number2),
         ]


usernames =[cses.cses_username, 
            lightoj.loj_username, 
            leetcode.lc_user, 
            hackerrank.payload['username'], 
            codeforces.user,
            toph.username,
            spoj.username,
            uva.username,
            timus.id,
            codechef.username,
            atcoder.username,
            vjudge.username_1,
            vjudge.username_2
            ]
urls = [cses.cses_url, 
        lightoj.loj_url, 
        'https://leetcode.com/'+leetcode.lc_user,
        'https://www.hackerrank.com/'+hackerrank.payload['username'],
        'https://codeforces.com/profile/'+codeforces.user,
        'https://toph.co/u/'+toph.username,
        'https://www.spoj.com/users/'+spoj.username,
        uva.profile_url,
        timus.url, 
        codechef.url,
        atcoder.profile_url,
        vjudge.url_1,
        vjudge.url_2
        ]

tot_all=0
for i in solved:
    tot_all+=int(i)

zipped_res=zip(oj_index, oj, solved, usernames,urls)  
sorted_res=sorted(zipped_res, key = lambda x: x[2],  reverse=True)
@app.route('/')
def index():
    return render_template('index.html',   oj_count_username_url=sorted_res, tot_all=tot_all)

# main driver function
if __name__ == '__main__': 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()