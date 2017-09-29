# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class QiDianPipeline(object):

    def __init__(self):

        self.connect = pymysql.connect(
            host='127.0.0.1',
            db='Scrapy_test',
            user='Your_User',
            passwd='Your_pass',
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        sql = 'insert into Scrapy_test.novel(name,author,intro) values (%s,%s,%s)'
        self.cursor.execute(sql, (item['name'], item['author'], item['intro']))
        self.connect.commit()
        return item

