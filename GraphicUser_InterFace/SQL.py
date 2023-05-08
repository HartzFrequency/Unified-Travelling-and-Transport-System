import mysql.connector

UTTSdb = mysql.connector.connect(
host='localhost',
user='root',
password='harsh',
database='UTTS')
cur=UTTSdb.cursor()

def Query_LoginCheck(username,password):
    Query="SELECT * FROM users WHERE first_name = '{}' AND Password = '{}'".format(username,password)
    cur.execute(Query)
    Result=cur.fetchall()
    return Result

def Query_GetAvailableFlight(frm,to):
    Query="SELECT flightNo,Name,Duration,type,capacity,fare FROM flight WHERE FromLocation='{}' AND ToLocation='{}'".format(frm,to)
    cur.execute(Query)
    Result=cur.fetchall()
    return Result

def Query_GetAvailableBus(frm,to):
    Query="SELECT BusID,Name,Duration,type,capacity,fare FROM Bus WHERE FromLocation='{}' AND ToLocation='{}'".format(frm,to)
    cur.execute(Query)
    Result=cur.fetchall()
    return Result

def Query_GetAvailableCar(frm,to):
    Query="SELECT CarID,Name,Duration,type,capacity,fare FROM Car WHERE FromLocation='{}' AND ToLocation='{}'".format(frm,to)
    cur.execute(Query)
    Result=cur.fetchall()
    return Result

def Query_GetAvailableTrain(frm,to):
    Query="SELECT PNR,Name,Duration,type,capacity,fare FROM train WHERE FromLocation='{}' AND ToLocation='{}'".format(frm,to)
    cur.execute(Query)
    Result=cur.fetchall()
    return Result

def Query_GetAvailableRailway(frm,to):
    Query="SELECT * FROM railways"
    cur.execute(Query)
    Result=cur.fetchall()
    return Result

def Query_GetAvailableTruck(frm,to):
    Query="SELECT * FROM trucks"
    cur.execute(Query)
    Result=cur.fetchall()
    return Result


def Query_WriteSearchResult(QueryContainer):
    with open("LocalDATA\\buffer_query_data.txt", "w") as f:
        for line in QueryContainer:
            f.write(str(line) + "\n")

def Query_FetchFromFile():
    Buffer = open('LocalDATA\\buffer_query_data.txt', 'r')
    Lines = Buffer.readlines()
    list = []
    for line in Lines:
        line = line.strip()
        line = line.strip("()")
        list.append(line)
    return list
