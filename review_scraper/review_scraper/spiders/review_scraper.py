import scrapy


class ReviewSpider(scrapy.Spider):
    name = "reviews"

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        urls = ['https://www.rottentomatoes.com/m/star_wars_the_last_jedi/reviews/?page=1&type=user&sort=']
        # for i in range(52):
        #     urls.append('https://www.rottentomatoes.com/m/star_wars_the_last_jedi/reviews/?page=%s&type=user&sort=' % (i))
        # print(urls)

        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        filename = 'rt_reviews.csv'
        with open(filename, 'wb') as f:
            f.write(str(response.css('div.review_table_row').extract()))
        self.log('Saved file %s' % filename)
