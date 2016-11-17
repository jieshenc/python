#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2

'''下载器
@version: 1.0
@author: Shenjie
@date: 2016-11-15
'''
class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        try:
            url_info = urllib2.urlopen(url)
            if url_info.getcode() != 200:
                return None
            return url_info.read()
        except:
            print 'download error url:%s' % url
            return None

