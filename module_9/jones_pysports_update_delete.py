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
#DEFINING VARIABLE TO ALLOW INNER JOIN PRINT
def show_players(cursor, title):

    # Inner Join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    #To print the full
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

#Establishing Connection and creating cursor for queries
try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    #INSERTING THE NEW PLAYER
    insert_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")
    new_player = ("Smeagol", "Shire Folk", 1)
    cursor.execute(insert_player, new_player)

    # Function ensure this commited before rest of data program
    db.commit()

    # Prints defined INNER JOINED TABLE
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # update the NEW PLAYER
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    cursor.execute(update_player)

    # shows update
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # delete query 
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)

    # show delete results
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
        
    else:
        print(err)
        
finally:
    db.close()   
