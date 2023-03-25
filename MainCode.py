import mysql.connector
UTTSdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='harsh',
    database='UTTS')
#print(UTTSdb.connection_id)
#print to check connection establishment
cur=UTTSdb.cursor()
s="CREATE TABLE users(UserID INT,first_name varchar(25),last_name varchar(25),birth_date DATE,phone varchar(15),address varchar(50),city varchar(20),state varchar(25),points INT)"
cur.execute(s)