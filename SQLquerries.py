DatabaseCreation='CREATE DATABASE UTTS'

UserTableCreation="CREATE TABLE users(UserID INT,first_name varchar(25),last_name varchar(25),birth_date DATE,phone varchar(15),address varchar(50),city varchar(20),state varchar(25),points INT)"

DataInsertion="INSERT INTO users(first_name,last_name,birth_date,phone,address,city,state) VALUES(%s,%s,%s,%s,%s,%s,%s)"
#cur.execute(s,VALUES)
#to execute one tuple

s="INSERT INTO users(first_name,last_name,birth_date,phone,address,city,state) VALUES(%s,%s,%s,%s,%s,%s,%s)"

Values=[("harsh","shrivastava","2003-06-05",8109288418,"Hathi Khana Road Morar","Gwalior","MP")]
#cur.executemany(s,Values)
#to insert many tuples we use this *list is passed 

ManyValues=[("harsh","shrivastava","2003-06-05",8109288418,"Hathi Khana Road Morar","Gwalior","MP")
    ("gauri","thakre","2003-11-30",9479675959,"Hostel no. 04, MITS","Gwalior","MP"),
    ("akhil","jain","2003-08-05",7456025891,"Dal Bazar","Gwalior","MP"),
    ("abhishek","rajput","2003-07-05",8109288418,"Hazira","Gwalior","MP"),
    ("shahrukh","khan","1992-01-09",8827344852,"Gandhi Chowk Bazar","Chatarpur","MP"),
    ("shraddha","kapoor","1985-08-30",6212418873,"Juhu","Mumbai","MH"),
    ("sunny","deol","1983-12-25",6748319921,"Jalianvala Bagh","Amritsar","Punjab"),
    ("hema","malini","1948-10-16",9828157533,"Kavi Bharti Nagar","Tiruchirapalli","Tamil Nadu"),
    ("jethalal","gada","2004-12-02",7852773891,"Phool Bagh","Gwalior","MP"),
    ("kartik","aryan","1995-02-14",7143143143,"Thatipur","Gwalior","MP")]
#cur.executemany(s,Values)
#UTTSdb.commit()

#Query to update
updatedata="UPDATE users SET price=price+10 WHERE price>200"
#cur.execute(updatedata)
#uttsdb.commit()

DeleteData="DELETE FROM users WHERE title='condition'"
#cur.execute(DeleteData)
#uutsdb.commit()

