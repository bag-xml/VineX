import mysql.connector
import config

cnx = mysql.connector.connect(user=config.USERNAME, password=config.PASSWORD,host=config.DBHOST,database=config.DATABASE)

def firstTimeAddition(username, password, email):
    print(f"[DB-Module] Initializing addUser Module")
    cursor = cnx.cursor()
    
    #checkers
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
    username_overlap = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
    email_overlap = cursor.fetchone()[0]
    
    if username_overlap > 0:
        print("[DB-Module] User specified an already existent username. Aborting account creation.")
        response = {
        "code": "",
        "data": 1,
        "success": False,
        "error": "error username"
        }

        return response
    elif email_overlap > 0:
        print("[DB-Module] User specified an already existent e-mail. Aborting account creation.")
        response = {
        "code": "",
        "data": 1,
        "success": False,
        "error": "error email"
        }

        return response
    else:
        print(f"[DB-Module] Filing database entry for a NEW USER. Given data is: {username} {email} {password}")
        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        cnx.commit()
        print(f"[DB-Module] User creation successful, welcome {username}!")
        cursor.close()
        userid = int(1)
        return username, userid