# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class CodeforcesPipeline:
#     def process_item(self, item, spider):
#         return item

# Remove unwanted Characters and spacing from the name value
class CodeForcesPipelines:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        availability_string = adapter.get('name')[0]
        if availability_string is not None:
            adapter['name'] = availability_string.strip()
        return item



# import mysql.connector
# class SaveToMySQLPipeline:

#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host = 'localhost',
#             user = 'root',
#             password = 'root',
#             database = 'cf'
#         )

#         ## Create cursor, used to execute commands
#         self.cur = self.conn.cursor()

#         ## Create books table if none exists
#         self.cur.execute("""
#         CREATE TABLE IF NOT EXISTS codeforces(
#             id int NOT NULL auto_increment, 
#             url VARCHAR(255),
#             name VARCHAR(255),
#             problem_rating VARCHAR(255),
#             solved_by VARCHAR(255)
#         )
#         """)

#     def process_item(self, item, spider):

#         ## Define insert statement
#         self.cur.execute(""" insert into codeforces (
#             url, 
#             name, 
#             problem_rating, 
#             solved_by
#             ) values (
#                 %s,
#                 %s,
#                 %s,
#                 %s
#             )""", (
#             item["url"],
#             item["name"],
#             item["problem_rating"],
#             item["solved_by"]
#         ))

#         # ## Execute insert of data into database
#         self.conn.commit()
#         return item


#     def close_spider(self, spider):

#         ## Close cursor & connection to database 
#         self.cur.close()
#         self.conn.close()