# coding:utf-8

import pymysql

db=pymysql.connect(host='localhost', user='root', password='12345678', port=3306)

# 游标
cursor = db.cursor()

# 创建数据库
cursor.execute("CREATE DATABASE IF NOT EXISTS school")
#
# # 创建表
sql = "CREATE TABLE IF NOT EXISTS school.students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL)"
cursor.execute(sql)

sql = "INSERT INTO school.students VALUES('1000', 'XiaoMin', 19)"
cursor.execute(sql)
# # 提交事物
db.commit()

sql = "SELECT * FROM school.students"
cursor.execute(sql)

students = cursor.fetchall()
print(students)

db.close()