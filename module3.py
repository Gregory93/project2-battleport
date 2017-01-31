import psycopg2

try:
    conn = psycopg2.connect("dbname=battleport user=postgres host=localhost password=gregory123")
except:
    print("cannot connect to the database")

cur=conn.cursor()
conn.set_isolation_level(0)

#cur.execute("INSERT INTO score (name,gamesp,gamesw,gamesl) \
      #VALUES ('Rens', 10, 4, 6)"); 
#cur.execute("UPDATE score set gamesp = gamesp + 1, gamesw = gamesw + 1 WHERE name='Gregory'")

#execute row WHERE rnum = 1
cur.execute("SELECT * FROM (SELECT *, row_number() OVER () as rnum FROM score ORDER BY rnum asc, gamesp desc, gamesw desc) ss WHERE rnum = 1")
rows = cur.fetchall()
for row in rows:
    print ("Name = ", row[0], "\n")

#execute row WHERE rnum = 2
cur.execute("SELECT * FROM (SELECT *, row_number() OVER () as rnum FROM score ORDER BY rnum asc, gamesp desc, gamesw desc) ss WHERE rnum = 2")
rows2 = cur.fetchall()
for row2 in rows2:
    print ("Name = ", row2[0], "\n")

#execute row WHERE rnum = 3
cur.execute("SELECT * FROM (SELECT *, row_number() OVER () as rnum FROM score ORDER BY rnum asc, gamesp desc, gamesw desc) ss WHERE rnum = 3")
rows3 = cur.fetchall()
for row3 in rows3:
    print ("Name = ", row3[0], "\n")

#execute row WHERE rnum = 4
cur.execute("SELECT * FROM (SELECT *, row_number() OVER () as rnum FROM score ORDER BY rnum asc, gamesp desc, gamesw desc) ss WHERE rnum = 4")
rows4 = cur.fetchall()
for row4 in rows4:
    print ("Name = ", row4[0], "\n")

#execute row WHERE name is TAHSIN   
cur.execute("SELECT * FROM (SELECT *, row_number() OVER () as rnum FROM score ORDER BY rnum asc, gamesp desc, gamesw desc) ss WHERE rnum = 5")
rows5 = cur.fetchall()
for row5 in rows5:
    print ("Name = ", row5[0], "\n")