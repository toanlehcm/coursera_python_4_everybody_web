# import sqlite3 as sql

# # conn = sqlite3.connect('database.db')
# # print("Opened database successfully");

# con = sql.connect("D:\Flask\database.db")
# con.row_factory = sql.Row

# # UPDATE students SET name = {name}, email = {email}, hometown = {hometown}, dob = {dob}, score = {score} WHERE id = {id};

# cur = con.cursor()
# id = 2
# name = "Thao Nguyen"
# email = "hungphu2639@gmail.com"
# hometown = "Binh Duong"
# dob = "25/08/2003"
# score = "10"
# # cur.execute("UPDATE students SET name = "?", email = "?", hometown = "?", dob = "?", score = "?" WHERE id = "?";",(name,email,hometown,dob,score,id))
# # cur.execute(f"UPDATE students SET name = '%s', email = '%s' WHERE id = %s;"%(name,email,id))
# cur.execute("UPDATE students SET name = %s, email = %s, hometown = %s, dob = %s, score = %s WHERE id = %s;"%(name,email,hometown,dob,score,id))

# # cur.execute("select * from students")

# rows = cur.fetchall()
# id_list = list()
# for row in rows:
    # id_list.append(row["email"])
    # # print(row["id"])
# print(id_list)
# con.commit()