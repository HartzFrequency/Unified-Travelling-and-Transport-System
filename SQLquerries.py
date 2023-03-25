DatabaseCreation='CREATE DATABASE UTTS'

UserTableCreation="CREATE TABLE users(UserID INT,first_name varchar(25),last_name varchar(25),birth_date DATE,phone varchar(15),address varchar(50),city varchar(20),state varchar(25),points INT)"

DataInsertion="INSERT INTO users(first_name,last_name,birth_date,phone,address,city,state) VALUES(%s,%s,%s,%s,%s,%s,%s)"
#cur.execute(s,VALUES)
#to execute one tuple

Values=[("harsh","shrivastava","2003-06-05",8109288418,"Hathi Khana Road Morar","Gwalior","MP")
    ]
#cur.executemany(s,Values)
#to insert many tuples we use this *list is passed 