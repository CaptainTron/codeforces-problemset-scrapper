## Codeforces Problemset Scrapper
This is a Scrapy-based web scraper specifically designed for extracting detailed information about Codeforces problems. The Codeforces API lacks certain details such as URLs, number of people who have solved the problems, and problem ratings. This scraper solves that problem by extracting data for better problem analysis. 



### Insights from the data  
Following topics are present (tags) in the problemset with number of problems.
```
{
    "2-sat": 34,
    "bitmasks": 559,
    "data structures": 1693,
    "dp": 2074,
    "graphs": 1045,
    "matrices": 119,
    "two pointers": 528,
    "strings": 714,
    "brute force": 1638,
    "constructive algorithms": 1706,
    "greedy": 2782,
    "implementation": 2681,
    "math": 2817,
    "number theory": 722,
    "binary search": 1030,
    "sortings": 1054,
    "combinatorics": 659,
    "games": 220,
    "hashing": 206,
    "interactive": 222,
    "dfs and similar": 914,
    "trees": 803,
    "dsu": 346,
    "divide and conquer": 283,
    "fft": 92,
    "geometry": 387,
    "string suffix structures": 90,
    "probabilities": 231,
    "meet-in-the-middle": 49,
    "ternary search": 53,
    "shortest paths": 262,
    "flows": 143,
    "*special problem": 437,
    "graph matchings": 89,
    "schedules": 10,
    "expression parsing": 36,
    "chinese remainder theorem": 16
}

Total problems:- 9678
Total types of problems:- 26744
```
use ```findproblems.py``` to find regarding your rating and topics  
```main.py```file is for analysis of problemset.



### Implemented Features
- Random headers for requests
- Storage in MySQL database
- Extraction of data from multiple pages
- Data cleaning and pre-processing for the following fields:
    - URL
    - Name
    - Number of people who have solved the problem
    - Problem rating
    - Tags
- Rotating proxy support (You need to provide your own URL, sign up [here](https://proxy2.webshare.io/) for a dashboard)

> [!NOTE]
> - Refer to the `output.json` file for the latest results as of 23rd July 2024.
> - To use this scraper, clone the repository and install the required dependencies using the `requirements.txt` file.
> - Run `scrapy crawl cf -O problems.json` for a JSON file or `problems.csv` for a CSV file.
> - Feel free to contribute additional features by creating pull requests.

> [!WARNING]
> - Be cautious when using this scraper as Codeforces may block your IP address. Consider using a rotating proxy for each request by adding the line `meta={"proxy":"protocol://yourusername:yourpassword@domainname:port/"}` in the `spiders/cf.py` file, specifically on line 27.


> [!TIP]
> 
