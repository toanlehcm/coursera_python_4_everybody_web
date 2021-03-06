from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')
    
@app.route('/')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    cur.execute("SELECT \"_rowid_\",* FROM \"main\".\"students\"  ORDER BY \"id\" ASC LIMIT 0, 49999;")

    rows = cur.fetchall()
    return render_template("list.html",rows = rows)

@app.route('/create')
def create():
    return render_template('create.html')
    
@app.route('/edit',methods = ['POST', 'GET'])
def update_form():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    cur.execute("SELECT \"_rowid_\",* FROM \"main\".\"students\"  ORDER BY \"id\" ASC LIMIT 0, 49999;")
    
    rows = cur.fetchall()
    
    return render_template("update_form.html",rows = rows)
    
    
@app.route('/update',methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        try:
            id = request.form['id']
            name = request.form['name']
            email = request.form['email']
            hometown = request.form['hometown']
            dob = request.form['dob']
            score = request.form['score']
            dict_info = {"name":name,"email":email,"hometown":hometown,"dob":dob,"score":score}
            with sql.connect("database.db") as con:
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute("SELECT * FROM students")
                
                rows = cur.fetchall()
                id_list = []
                for row in rows:
                    id_list.append(row["id"])
                if id not in id_list:
                    cur.execute("INSERT INTO students (id,name,email,hometown,dob,score) \
                       VALUES (?,?,?,?,?,?)",(id,name,email,hometown,dob,score) )
                else:
                    list_key = []
                    list_value = []
                    for values in dict_info.values():
                        list_value.append(values)
                    for key in dict_info.keys():
                        list_key.append(key)
                        
                    for i in list_value:
                        if i == "":
                            pass
                        else:
                            key = (list_key[list_value.index(i)])
                            cur.execute("UPDATE students SET %s = '%s' WHERE id = %s;"%(key,i,id))
                con.commit()
        except:
            con.rollback()
            
        finally:
            con = sql.connect("database.db")
            con.row_factory = sql.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM students")
            cur.execute("SELECT \"_rowid_\",* FROM \"main\".\"students\"  ORDER BY \"id\" ASC LIMIT 0, 49999;")

            rows = cur.fetchall()
            return render_template("list.html",rows = rows)

@app.route('/delete_form',methods = ['POST', 'GET'])
def delete_form():

    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    cur.execute("SELECT \"_rowid_\",* FROM \"main\".\"students\"  ORDER BY \"id\" ASC LIMIT 0, 49999;")

    rows = cur.fetchall()
    return render_template('delete_form.html',rows = rows)
    
@app.route('/delete',methods = ['POST', 'GET'])
def delete():
    if request.method == 'POST':
        try:
            id = request.form['id']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM students WHERE id = %s"%id, )

            con.commit()
        except:
            con.rollback()
            
        finally:
            con = sql.connect("database.db")
            con.row_factory = sql.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM students")
            cur.execute("SELECT \"_rowid_\",* FROM \"main\".\"students\"  ORDER BY \"id\" ASC LIMIT 0, 49999;")

            rows = cur.fetchall()
            return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)