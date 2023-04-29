import mysql.connector
UTTSdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='harsh',
    database='UTTS')
cur=UTTSdb.cursor()

Query="SELECT CarID,Name,Duration,type,capacity,fare FROM car WHERE FromLocation='GWL' AND ToLocation='DLH'"
cur.execute(Query)
availableCAR=cur.fetchall()
print(availableCAR)

# with open(r'buffer_query_data.txt', 'w') as fp:
#     for item in availableCAR:
#         # write each item on a new line
#         fp.write("%s\n" % item)
#     print('Done')

data = [(1, 'Car 1', 'DI', 4, 500), 
        (20, 'Car 20','EV', 4, 500)]

# with open("INprogressCode\\buffer_query_data.txt", "w") as f:
#     for line in availableCAR:
#         f.write(str(line) + "\n")

# Using readlines()
file1 = open('INprogressCode\\buffer_query_data.txt', 'r')
Lines = file1.readlines()

list = []

for line in Lines:
    line = line.strip()
    line = line.strip("()")
    list.append(line)
    # print("{}".format(line))
print(list)