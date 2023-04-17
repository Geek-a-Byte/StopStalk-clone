# StopStalk-clone
A static problem-solving profile creator for portfolio building
- [x] scraped data of individual sites
- [x] scraped vjudge excluding the individual sites

### ``Install``
- fork and clone the repository
- fillup the .env-copy file and rename it to .env

```py
cf_api_key = '<create and copy api key using your codeforces account and paste it here>'
cf_api_secret = '<create and copy api secret using your codeforces account and paste it here>'
```

- replace the usernames in each oj folder under scrapers
- do not commit the .env file to github for privacy purposes of your password and api keys, add it to .gitignore instead
- push your changes (username, env file) to github and deploy with render 

![ss](https://user-images.githubusercontent.com/59027621/232550423-f66ca106-d560-4d75-ad90-9769cd314bef.png)


### ``additional resources``
-  https://blog.gitguardian.com/how-to-handle-secrets-in-python/
