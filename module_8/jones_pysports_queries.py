#import MYsql
import mysql.connector
from mysql.connector import errorcode
#Set database config
config = {
    "user": "quincy",
    "password": "TX1993",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
    }
#Establishing Connection and creating cursor for queries
try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    #Teams query
    teams = cursor.fetchall()
    print("--DISPLAYING TEAM RECORDS--")
    
    for team in teams:
        print("Team Name: {}".format(team[1]))
    #Players Query
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()
    print("\n --DISPLAYING PLAYER RECORDS--")
    for player in players:
        print(" Player ID: {}\n First Name{}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
        
    else:
        print(err)
        
finally:
    db.close()   
