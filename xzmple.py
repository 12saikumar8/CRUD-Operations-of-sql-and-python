import mysql.connector

mysqldb=mysql.connector.connect(host="localhost",user="root",password="Saikumar1@",database="Xampledb")

mysqlcursor=mysqldb.cursor()

# mysqlcursor.execute("CREATE DATABASE Xampledb")

# mysqlcursor.execute("create table sae_data(id int primary key, name varchar(30), course varchar(5))")

# insert values

# try:

#     mysqlcursor.execute("insert into sae_data(id,name,course) values(1,'vinod','EEE')")
#     mysqldb.commit()
# except:
#     mysqldb.rollback()
# mysqldb.close()

# mysqlcursor.execute("insert into sae_data(id,name,course) values (3,'sai_Kumar','EEE')")
# mysqldb.commit()

# mysqlcursor.execute("select * from sae_data where id=1")
# result=mysqlcursor.fetchall()
# for i in result:
#         id =i[0]
#         name=i[1]
#         course=i[2]
#         print(id,name,course)
# print(result)

#UPDATE the values
# mysqlcursor.execute("update sae_data set name='aditya',course='ECE' where id=3")
# mysqldb.commit()


# DELETE

mysqlcursor.execute("delete from sae_data where id=1")
mysqldb.commit()
