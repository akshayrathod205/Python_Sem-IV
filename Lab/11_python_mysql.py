import mysql.connector as sql

try:
    connection=sql.connect(
        user="root",
        password="Root@1234",
        host="localhost",
        port="5500",
        database="books"
    )
    if(connection.is_connected()):
        print("Connection established")

except Exception as e:
    print("Connection cannot be established")

cursor = connection.cursor()

query="create table booksdata(\
    id int primary key auto_increment,\
    title varchar(30),\
    author varchar(30),\
    publication varchar(50),\
    yearofpublication int,\
    price int\
    );"

try:
    cursor.execute(query)
    connection.commit()
except Exception as e:
    print(e)

insert_query="insert into booksdata(title,author,publication,yearofpublication,price) values (%s,%s,%s,%s,%s)"

values=[('Cryptography','A','AX',2000,1000), ('Alchemist','B','BX',2014,1200), ('Deep Thinking','C','CX',2003,3000), ('Data Structures', 'D', 'DX', 2022, 800)]
try:
    cursor.executemany(insert_query,values)
    connection.commit()

except Exception as e:
    print("Table insertion not done")

data_query="select * from booksdata"

try:
    cursor.execute(data_query)
    d1 = cursor.fetchall()
    print("Data:\n")

    for i in d1:
        print(i)

except Exception as e:
    print(e)

search_query1="select * from booksdata where publication='TMH' "

try:
    cursor.execute(search_query1)
    s1 = cursor.fetchall()
    print("\n\n\n searched pika is :")

    for i in s1:
        print(i)
except Exception as e:
    print(e)

search_query1="select * from booksdata where yearofpublication between 2001 and 2020 "

try:
    cursor.execute(search_query1)
    s1 = cursor.fetchall()
    print("\n\n\n searched pika is :")

    for i in s1:
        print(i)
except Exception as e:
    print(e)

update_query="update booksdata set price=600 where title='crpytography'"

try:
    cursor.execute(update_query)
    print("Data updated successfully")
    connection.commit()
except Exception as e:
    print(e)

delete_query="delete from booksdata where yearofpublication < 1980"

try:
    cursor.execute(delete_query)
    print("Data deleted successfully")
    connection.commit()
except Exception as e:
    print(e)