"""
数据库写操作示例
"""
import re
import pymysql
word_list=[]
def get_data():
    file01 =open("/home/tarena/aaa/dict.txt","r")
    values1= file01.read()
    word = re.findall(r"(\w+)\s+(.*)",values1)
    

    for item in word:
        word_list.append(item[0])
        # print(item[1])
    print(len(word_list))
###-------------------------------###
args ={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"dict",
    "charset":"utf8"
}

# 连接数据库
db = pymysql.connect(**args)
cur = db.cursor()
# 操作数据 --写
try:
    sql="insert into words (word,mean)values(%s,%s);"
    cur.executemany(sql,word_list)
    db.commit() # 提交写操作
except Exception as e:
    print(e)
    db.rollback()
# 关闭数据
cur.close()
db.close()