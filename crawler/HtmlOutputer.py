#!/usr/bin/python
# -*- coding: utf-8 -*-

'''HTML 输出器
@version: 1.0
@author: Shenjie
@date: 2016-11-15
'''
class HtmlOutputer(object):

    def __init__(self):
        self.html_data = []

    def addToOutputContent(self, html_content):
        if html_content is None:
            return
        self.html_data.append(html_content)

    def output(self):
        if self.html_data is None or len(self.html_data) == 0:
            return
        fo = open("output.html", "w")
        fo.write("<html>")
        fo.write("<body>")
        fo.write("<table>")
        for data in self.html_data:
            fo.write("<tr>")
            fo.write("<td>%s</td>" % data['url'])
            fo.write("<td>%s</td>" % data['title'].encode("utf-8"))
            fo.write("<td>%s</td>" % data['html_content'].encode("utf-8"))
            fo.write("</tr>")
        fo.write("</table>")
        fo.write("</body>")
        fo.write("</html>")
        fo.close()

