#!/usr/bin/python
# -*- coding: utf-8 -*-

'''url 管理器
@version: 1.0
@author: Shenjie
@date: 2016-11-15
'''
class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def addNewUrl(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def addNewUrls(self, urls):
        if urls is None or len(urls) <= 0:
            return
        for url in urls:
            self.addNewUrl(url)

    def hasNewUrl(self):
        return self.new_urls != 0

    def getNewUrl(self):
        if self.new_urls is None or len(self.new_urls) <= 0:
            return None
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


        

