import scrapy


class ReviewSpider(scrapy.Spider):
    """Class for instance of Scrapy Web-Crawler."""
    name = "force_awakens_reviews"

    def start_requests(self):
        """Generate scraped webpage content."""

        # Iterate over proper amount of pages and use the numbered index to
        # build a list of all urls you want the scraper to target.

        urls = []
        for i in range(1, 52):
            url = 'https://www.rottentomatoes.com/m/star_wars_episode_vii_the_force_awakens/reviews/?page=' + str(i) + '&type=user&sort='
            urls.append(url)

        # After the list is built, the parse() method is then called on each
        # url (which writes the CSV file).

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Write generated scraped content to CSV file."""

        # Create new CSV file if it does not exist, if it does open it and
        # append new information.

        f = open('newest_force_awakens_reviews.csv', 'a+')
        for review in response.css('div.review_table_row'):

            # The above line is iterating over every review on the individual
            # page of HTML in the response (using the urls variable we defined)
            # Now, using the reviews on a given page, we must create variables
            # that represent different aspects of the review. We do this below.

            user_review = review.css('div.user_review')
            star_rating = review.css('div.scoreWrapper').css('span')
            username = review.css('span')
            user_link = review.css('a').xpath('@href').extract()[0]
            date_review = review.css('span.fr').extract()[0]
            superreviewer_status = review.css('div.superreviewer').extract()[0]

            # Using the variables defined above, write in proper format to a
            # CSV file.

            f.write(user_review.extract()[0].split('</div>')[1].replace(',', '').replace(';', '') + ', ')
            try:
                f.write(str(float(star_rating.extract()[0].split('"')[1]) / 10) + ', ')
            except ValueError:
                f.write(star_rating.extract()[0].split('"')[1] + ', ')
            f.write(username.extract()[0].split('>')[1].split('<')[0] + ', ')
            f.write('https://www.rottentomatoes.com' + user_link + ', ')
            f.write(date_review.strip('<span> class="fr small subtle">,</').replace(',', '') + ', ')
            if superreviewer_status.strip('<div class="col-sm-7 col-xs-9 top_critic col-sm-push-13 superreviewer"></div>'):
                f.write('Super-reviewer')
            else:
                f.write('N/A')
            f.write('\n')
        f.close()
