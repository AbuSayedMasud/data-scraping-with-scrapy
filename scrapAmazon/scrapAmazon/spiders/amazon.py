import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456&ref=nav_em__nav_desktop_sa_intl_computer_accessories_and_peripherals_0_2_6_2']
    print("==============>")

    def parse(self, response):
        products = response.css('.s-card-container')
        for product in products:
            # url="https://www.amazon.com"
            # page_links= url+product.css('.a-link-normal.s-no-outline').attrib['href']
            
            # # print(page_links)
            # yield response.follow(page_links,callback=self.product_details)
            yield {
                'title':product.css('div a .a-size-base-plus::text').get(),
                    'image':product.css('div.a-section img').attrib['src'],
                    'price':product.css('div .a-price-whole::text').get(),

                    
                    'review':product.css('div span .a-size-base::text').get(),
                    'numberOfreview':product.css('div span .s-underline-text::text').get(),
                    'sellerType':product.css('div span .a-badge-text::text').get(),
                    # 'link':product.css('.a-link-normal.s-no-outline').attrib['href'],
            }
        next_page = response.css('a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator::attr(href)').get()
        if next_page is not None:
          next_page = response.urljoin(next_page)
          yield scrapy.Request(next_page, callback=self.parse) 
    # def product_details(self, response):
    #     items = response.selector.xpath('/html/body/div[1]/div[2]/div[9]/div[6]/div[4]')
    #     for item in items:
           
    #         yield{
               
    #             'Title' : item.css('#productTitle::text').get(),
    #             'answered_questions' : item.css('.a-size-base::text').get(),
               
    #             'individualPrice':item.css('.a-offscreen::text').get(),
                
               
                   

    #         }
        
            
            

