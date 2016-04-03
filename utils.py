import sqlite3

#if valid cred, return user_id
#else return -1
def auth(user, pw):
	conn = sqlite3.connect("app.db", check_same_thread=False)
	c = conn.cursor()
	q = "SELECT rowid FROM users where username = ? and pw = ?;"
	c.execute(q, (user, pw) )
	result = c.fetchall()
	if len(result) == 1:
		return result[0][0]
	conn.close()
	return -1

#Checks if user exists in the database
#If not, add them
def addUser(user, pw, email, instrument, location, photo, user_type):
	conn = sqlite3.connect("app.db", check_same_thread=False)
	c = conn.cursor()
	c.execute("SELECT rowid FROM users where username = ?;", (user))
	result = c.fetchall()
	if len(result) > 0:
		return False # user already exists
	c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?);", (user, pw, email, NULL, instrument, location, photo, user_type))
	conn.commit()
	conn.close()
	return True

def addEvent(user, location, instrument):
    conn = sqlite3.connect("app.db", check_same_thread=False)
    c = conn.cursor()
    c.execute(" users", (user))
