# StopStalk-clone
A static problem-solving profile creator for portfolio building
- [x] scraped data of individual sites
- [x] scraped vjudge excluding the individual sites

### ``Install``
- fork and clone the repository
- fillup the .env-copy file and rename it to .env

```py
hr_password='<hackerrank-password>'

cf_api_key = '<create and copy api key using your codeforces account and paste it here>'
cf_api_secret = '<create and copy api secret using your codeforces account and paste it here>'
```

- replace the usernames in each oj folder under scrapers
- do not commit the .env file to github for privacy purposes of your password and api keys, add it to .gitignore instead
- push your changes (username, env file) to github and deploy with render 

![image](https://user-images.githubusercontent.com/59027621/232427926-4643aed2-cea5-4fa0-b59b-d8fa01cf1cb5.png)

### ``additional resources``
-  https://blog.gitguardian.com/how-to-handle-secrets-in-python/
