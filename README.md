## Codeforces Problemset Scrapper
This is a Scrapy-based web scraper specifically designed for extracting detailed information about Codeforces problems. The Codeforces API lacks certain details such as URLs, number of people who have solved the problems, and problem ratings. This scraper solves that problem by extracting data for better problem analysis. 

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
