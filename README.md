## Codeforces Problemset Scrapper
This is a web scapper, developed with Scrapy, specifically for scrapping the problems of codeforces, the api provided doesn't provide much of details like urls, no. of people solved that problems, and rating of problems. So I've developed
this scrapper to extract data to better analyze problems so that we can solve fewer and good problems (since quality of questions also depends on no. of people solved and rating of problems). 
>- You can add more features by creating PRs.

To use this scrapper just clone this repo and install the requirement.txt file  
On the command shell type ```scrapy crawl cf -O problmes.json``` for json file or ```problems.csv``` for csv file

#### Features Implemented
- Random Headers
- MySql storage
- Data cleaning (for name field)
- Rotating Proxy (You've to use your own url for it, signup here for [dashboard](https://proxy2.webshare.io/)



> [!NOTE]
> - See the output.json file for result as on 23-july-2024.

> [!WARNING]
> - You can get blocked by Codeforces so better to use rotating-proxy in each request, you can add it in your own, simple put line ```meta={"proxy":"protocol://username:password@domainname:PORT"}``` in file spiders/cf.py line 27.
