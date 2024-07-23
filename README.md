## Codeforces Problemset Scrapper
This is a web scapper, developed with Scrapy, specifically for scrapping the problems of codeforces, the api provided doesn't provide much of details like urls, no. of people solved that problems, and rating of problems. So I've developed
this scrapper to extract data to better analyze problems so that we can solve fewer and good problems (since quality of questions also depends on no. of people solved and rating of problems). 
>- You can add more features by creating PRs.

To learn about scrapy you can [Click here](https://docs.scrapy.org/en/latest/intro/overview.html)

To use this scrapper just clone this repo and install the requirement.txt file  
On the command shell type ```scrapy crawl cf -O problmes.json``` or problems.csv for csv file
