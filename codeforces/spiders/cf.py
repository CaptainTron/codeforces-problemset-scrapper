import scrapy
from codeforces.items import CodeforcesProblemSet

class CfSpider(scrapy.Spider):
    name = "cf"
    allowed_domains = ["codeforces.com"]
    start_urls = ["https://codeforces.com/problemset"]

    #Parse the Item from Here.....
    def parse(self, response):
        table = response.css('table.problems')
        rows = table.css('tr')
        cf = CodeforcesProblemSet()
        for row in rows:
            if row is not None:
                cf['url'] = "https://codeforces.com/" + str(row.css('td:nth-child(1) a ::attr(href)').get()),
                cf['name'] =  row.css('td:nth-child(2) a::text').get(),
                cf['problem_rating'] =  row.css('td:nth-child(4) span.ProblemRating::text').get(),
                cf['solved_by'] =  row.css('td:nth-child(5) a::text').get(),
                yield cf

        
        page = response.css('div.pagination')
        next_page_url = "https://codeforces.com" + page.css('li:last-child a ::attr(href)').get()
        print("#####################" + next_page_url + "######################")
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)
