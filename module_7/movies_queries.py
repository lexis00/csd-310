import mysql.connector
from mysql.connector import errorcode #Importing mysql connector

#Creating a dictionary to configure database user setting 
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

#Testing connection

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MYSQL on host {} with database {}".format(config["user"],config["host"],config["database"]))
    input("\n\n Press enter to continue...\n")

    cursor = db.cursor()
    cursor.execute("SELECT studio_id, studio_name FROM studio") 
    studio = cursor.fetchall()
    print("Displaying Studio RECORDS")
    for studio in studio:
        print("Studio ID: {}\nStudio Name:{}\n".format(studio[0], studio[1]))

    cursor = db.cursor()
    cursor.execute("SELECT genre_id, genre_name FROM genre") 
    genre = cursor.fetchall()
    print("Displaying Genre RECORDS")
    for genre in genre:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    cursor = db.cursor()
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <= 200") 
    film = cursor.fetchall()
    print("Displaying Short Film RECORDS")
    for film in film:
        print("Film Name: {}\nRuntime: {}\n".format(film[0],film[1]))

    cursor = db.cursor()
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director, film_name") 
    film = cursor.fetchall()
    print("Displaying Director RECORDS in Order")
    for film in film:
        print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))

    


    

except mysql.connector.Error as err:
    if err.errno == errorcode.ER.ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" This specified database does not exist")

    else: 
        print(err)

finally: 
    db.close()

