#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urlparse

'''HTML 解析器
@version: 1.0
@author: Shenjie
@date: 2016-11-15
'''
class HtmlParser(object):

    def _get_new_url(self, html_url, soup):
        self.new_urls = []
        if html_url is None or soup is None:
            return None
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            link_url = link['href']
            link_full_url = urlparse.urljoin(html_url, link_url)
            self.new_urls.append(link_full_url)

        return self.new_urls

    def _get_new_data(self, html_url, soup):
        if html_url is None or soup is None:
            return None
        new_datas = {}
        new_datas['url'] = html_url
        title = soup.find("dd", {"class":"lemmaWgt-lemmaTitle-title"}).find("h1")
        new_datas['title'] = title.get_text()
        content = soup.find("div", {'class':"lemma-summary"})
        new_datas['html_content'] =  content.get_text()
        return new_datas

    
    def parse(self, html_url, html_data):
        if html_data is None:
            return None
        soup = BeautifulSoup(html_data, 'html.parser')
        new_urls = self._get_new_url(html_url, soup)
        new_data = self._get_new_data(html_url, soup)
        return new_urls, new_data


