import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)
USERNAME = "''"    
PASSWORD = "''"

mycursor = db.cursor()
BANNED_CHARACTERS = r"['\";=#--]+"

if " " not in USERNAME and " " not in PASSWORD:
    query = (
        "SELECT forum_111.USERLOG.UserId_ "
        "FROM forum_111.USERLOG "
        "WHERE forum_111.USERLOG.Username_ = " + USERNAME +
        " AND forum_111.USERLOG.Password_ = " + PASSWORD + ";"
    )

    mycursor.execute(query)
    result = mycursor.fetchone()
    print(result)
else:
    print("Invalid input")

