import scrapy


class ReviewSpider(scrapy.Spider):
    """Class for instance of Scrapy Web-Crawler."""

    name = "reviews"

    def start_requests(self):
        """Generate scraped webpage content."""

        urls = []
        for i in range(1, 52):
            url = 'https://www.rottentomatoes.com/m/star_wars_the_last_jedi/reviews/?page=' + str(i) + '&type=user&sort='
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Write generated scraped content to CSV file."""

        f = open('newest_reviews.csv', 'a+')
        for review in response.css('div.review_table_row'):
            user_review = review.css('div.user_review')
            star_rating = review.css('div.scoreWrapper').css('span')
            username = review.css('span')
            user_link = review.css('a').xpath('@href').extract()[0]
            # TODO: Add in date for review
            # TODO: Add in superreviewer status for review, if present.
            f.write(user_review.extract()[0].split('</div>')[1].replace(',', '').replace(';', '') + ', ')
            try:
                f.write(str(float(star_rating.extract()[0].split('"')[1]) / 10) + ', ')
            except ValueError:
                f.write(star_rating.extract()[0].split('"')[1] + ', ')
            f.write(username.extract()[0].split('>')[1].split('<')[0] + ', ')
            f.write('https://www.rottentomatoes.com' + user_link)
            f.write('\n')
        f.close()
