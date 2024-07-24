import scrapy
from codeforces.items import CodeforcesProblemSet

class CfSpider(scrapy.Spider):
    name = "cf"
    allowed_domains = ["codeforces.com"]
    start_urls = ["https://codeforces.com/problemset"]

    def parse(self, response):
        table = response.css('table.problems')
        rows = table.css('tr')
        cf = CodeforcesProblemSet()
        for row in rows:
            if row is not None:
                cf['url'] = "https://codeforces.com/" + str(row.css('td:nth-child(1) a ::attr(href)').get()),
                cf['name'] =  row.css('td:nth-child(2) a::text').get(),
                
                cf['tags'] = []
                # append the tags to the list
                for tags in row.css('td:nth-child(2) div:nth-child(2) a::text').getall():
                    cf['tags'].append(tags)
                
                cf['problem_rating'] =  row.css('td:nth-child(4) span.ProblemRating::text').get(),
                cf['solved_by'] =  row.css('td:nth-child(5) a::text').get(),
                yield cf

        page = response.css('div.pagination')
        next_page_url = "https://codeforces.com" + page.css('li:last-child a ::attr(href)').get()
        print("##################### " + next_page_url + " ######################")
        # Jump to the next page of the pagination if it exist
        if next_page_url is not None:
            # append your rotating proxy here with meta={'proxy': 'http://proxy:port'}
            yield response.follow(next_page_url, callback=self.parse)
