import scrapy


class ReviewSpider(scrapy.Spider):
    name = "reviews"

    def start_requests(self):
        # headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        urls = []
        for i in range(1, 52):
            url = 'https://www.rottentomatoes.com/m/star_wars_the_last_jedi/reviews/?page=' + str(i) + '&type=user&sort='
            urls.append(url)

        # for url in self.start_urls:
            # yield scrapy.Request(url, headers=headers, callback=self.parse)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('=')[1][0:2]
        filename = 'rt_reviews_%s.csv' % page
        with open(filename, 'wb') as f:
            f.write(page)
            f.write(str(response.css('div.review_table_row').extract()))
        self.log('Saved file %s' % filename)
