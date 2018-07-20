# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class LolPipeline(object):
    def process_item(self, item, spider):
        # print()
        return item

class MySQLPipeline(object):
    """
    pymyql
    """
    def __init__(self):
        """
        连接数据库
        """
        self.conn = pymysql.connect(host='127.0.0.1',
                                    port=3306,
                                    user='root',
                                    password='zl2015',
                                    db='spider',
                                    charset='utf8'
        )
        self.cursor = self.conn.cursor()


    def process_item(self,item,spider):
        """
        把每条数据插入数据库
        """

        sql = "insert into lol(enName,name,shortName,story) values(%s,%s,%s,%s);"
        self.cursor.execute(sql,(item['enName'],item['name'],item['shortName'],item['story']))
        self.conn.commit()
        return item


    def close_spider(self,spider):
        """
        关闭数据库连接
        """
        self.cursor.close()
        self.conn.close()
