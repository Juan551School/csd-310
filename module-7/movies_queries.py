# Juan Macias Vasquez
# Date 06/28/2025
# Module 6.2 JSON Practice
# movies_queries.py

import mysql.connector
from mysql.connector import errorcode

# Connect to the database
try:
    db = mysql.connector.connect(
        host="localhost",       # hostname
        user="root",   # MySQL username
        password="Powerful@2025", # MySQL password
        database="movies"       # Movies Database
    )
    cursor = db.cursor()

    # 1. Display Studio Records
    print("-- DISPLAYING Studio RECORDS --")
    query = "SELECT studio_id, studio_name FROM studio"
    cursor.execute(query)
    studios = cursor.fetchall()
    for studio in studios:
        print("Studio ID: {}".format(studio[0]))
        print("Studio Name: {}\n".format(studio[1]))

    # 2. Display Genre Records
    print("-- DISPLAYING Genre RECORDS --")
    query = "SELECT genre_id, genre_name FROM genre"
    cursor.execute(query)
    genres = cursor.fetchall()
    for genre in genres:
        print("Genre ID: {}".format(genre[0]))
        print("Genre Name: {}\n".format(genre[1]))

    # 3. Display Short Film Records (Runtime < 120 minutes)
    print("-- DISPLAYING Short Film RECORDS --")
    query = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"
    cursor.execute(query)
    short_films = cursor.fetchall()
    for film in short_films:
        print("Film Name: {}".format(film[0]))
        print("Runtime: {}\n".format(film[1]))

    # 4. Display Director Records in Order
    print("-- DISPLAYING Director RECORDS in Order --")
    query = """
    SELECT film_name, film_director 
    FROM film
    ORDER BY film_director
    """# MySQL Command Line: Select Query:
    cursor.execute(query)
    directors = cursor.fetchall()
    for film in directors:
        print("Film Name: {}".format(film[0]))
        print("Director: {}\n".format(film[1]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The database does not exist")
    else:
        print(err)
finally:
    cursor.close()
    db.close()

