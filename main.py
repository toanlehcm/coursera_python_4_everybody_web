from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    cur.execute(
        "SELECT \"_rowid_\",* FROM \"main\".\"students\"  ORDER BY \"id\" ASC LIMIT 0, 49999;")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/store', methods=['POST', 'GET'])
def store():
    if request.method == 'POST':
        try:
            id = request.form['id']
            name = request.form['name']
            email = request.form['email']
            hometown = request.form['hometown']
            dob = request.form['dob']
            score = request.form['score']
            dict_info = {"name": name, "email": email,
                         "hometown": hometown, "dob": dob, "score": score}
            with sql.connect("database.db") as con:
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute("INSERT INTO students (id, name, email, hometown, dob, score) VALUES (?,?,?,?,?,?)",
                            (id, name, email, hometown, dob, score))
                con.commit()
        except:
            con.rollback()

        finally:
            con = sql.connect("database.db")
            con.row_factory = sql.Row

            cur = con.cursor()
            cur.execute("select * from students")
            cur.execute(
                "select \"_rowid_\",* from \"main\".\"students\" order by \"id\" asc limit 0, 49999;")

            rows = cur.fetchall()
            return render_template("list.html", rows=rows)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE id =%s" % id,)

    rows = cur.fetchall()

    return render_template("edit.html", rows=rows)


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        try:
            id = request.form['id']
            name = request.form['name']
            email = request.form['email']
            hometown = request.form['hometown']
            dob = request.form['dob']
            score = request.form['score']
            dict_info = {"name": name, "email": email,
                         "hometown": hometown, "dob": dob, "score": score}

            with sql.connect("database.db") as con:
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute("SELECT * FROM students WHERE id =%s" % id,)

                rows = cur.fetchall()

                list_key = []
                list_value = []
                for key in dict_info.keys():
                    list_key.append(key)
                for values in dict_info.values():
                    list_value.append(values)

                for i in list_value:
                    if i == "":
                        pass
                    else:
                        key = (list_key[list_value.index(i)])
                        cur.execute(
                            "UPDATE students SET %s = '%s' WHERE id = %s;" % (key, i, id))
                con.commit()
        except:
            con.rollback()

        finally:
            con = sql.connect("database.db")
            con.row_factory = sql.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM students")
            cur.execute(
                "SELECT \"_rowid_\",* FROM \"main\".\"students\"  ORDER BY \"id\" ASC LIMIT 0, 49999;")

            rows = cur.fetchall()
            return render_template("list.html", rows=rows)


@app.route('/delete_form', methods=['POST', 'GET'])
def delete_form():

    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    cur.execute(
        "SELECT \"_rowid_\",* FROM \"main\".\"students\"  ORDER BY \"id\" ASC LIMIT 0, 49999;")

    rows = cur.fetchall()
    return render_template('delete_form.html', rows=rows)


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        try:
            id = request.form['delete_id']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM students WHERE id = %s" % id,)

            con.commit()
        except:
            con.rollback()

        finally:
            con = sql.connect("database.db")
            con.row_factory = sql.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM students")
            cur.execute(
                "SELECT \"_rowid_\",* FROM \"main\".\"students\"  ORDER BY \"id\" ASC LIMIT 0, 49999;")

            rows = cur.fetchall()
            return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
