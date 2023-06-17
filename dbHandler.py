import sqlite3 as sql

database = "database.db"

def retrieve_user(username):
    con = sql.connect(database)
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    data = cur.fetchall()
    con.close()
    return data[0]

def create_user(username, hashed_password, salt):
    con = sql.connect(database)
    cur = con.cursor()
    cur.execute("INSERT INTO users (username, password, salt) VALUES (?,?, ?)", (username,hashed_password,salt))
    con.commit()
    con.close()

def check_duplicate_user(username):
    try:
        retrieve_user(username)
        print("Username taken. Please choose another username.")
        return True

    except:
        return False
