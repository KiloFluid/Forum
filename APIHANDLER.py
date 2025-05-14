import mysql.connector
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware ## This connect JS with PYTHON

app = FastAPI()

app.add_middleware( ## WHO CONTROLS THE MIDDLE
    CORSMiddleware, ## WHICH LIBARY TO USED
    allow_origins=["*"], ## WHO CAN ACCESS THE API
    allow_credentials=True, ## TELL THE API THE COOKIES AND ETC
    allow_methods=["*"], ## ALLOW WHICH METHODS
    allow_headers=["*"], ## Allow custom headers
)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "---"
)
USERNAME = "'---'"    # strings must be quoted for SQL
PASSWORD = "'---'"




@app.get("/")
def read_root():
    mycursor = db.cursor()
    BANNED_CHARACTERS = """[\";=#--]+"""

    # Avoid 1==1. This is a security hole.
    Failed = True
    for string in BANNED_CHARACTERS:
        if string in USERNAME or string in PASSWORD:
            Failed =False
    if " " not in USERNAME and " " not in PASSWORD:
        query = (
            "SELECT forum_111.USERLOG.UserId_ "
            "FROM forum_111.USERLOG "
            "WHERE forum_111.USERLOG.Username_ = " + USERNAME +
            " AND forum_111.USERLOG.Password_ = " + PASSWORD + ";"
        )

        mycursor.execute(query)
        result = list(mycursor.fetchone())
        print(result[0])
        return {"Data": result[0]} ## Returns this
    else:
        return {"Data": "Invalid input"} ## Returns this


    


