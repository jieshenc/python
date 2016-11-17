#!/usr/bin/python
# -*- conding: utf-8 -*-

import UrlManager, HtmlDownloader, HtmlParser, HtmlOutputer

class Crawler(object):

    def __init__(self):
        self.url_manager = UrlManager.UrlManager()
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
        self.outputer = HtmlOutputer.HtmlOutputer()

    def craw(self, root_url):
        count = 0
        self.url_manager.addNewUrl(root_url)
        while self.url_manager.hasNewUrl(): 
            new_url = self.url_manager.getNewUrl();
            print "craw %d %s" % (count, new_url)
            download_data = self.downloader.download(new_url)
            new_urls, html_content = self.parser.parse(new_url, download_data)
            self.url_manager.addNewUrls(new_urls)
            self.outputer.addToOutputContent(html_content)
            if count > 10:
                break
            count = count + 1

        self.outputer.output()


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/link?url=-dnj4ugiXrVxNvaPZ8EzlYGAIq766kBiZVlzQBZiGVZV9U92c8sm0H_FVeJXTbHhOHJB9ZZ0qDgKlBHSuelzia"
    crawler = Crawler()
    crawler.craw(root_url)
