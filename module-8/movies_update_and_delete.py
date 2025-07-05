# Juan Macias Vasquez
# Date 07/05/2025
# Module 8.2 Movies:Update & Deletes
# movies_update_and_delete.py

import mysql.connector

def show_films(cursor, title):
    # SQL query to get film name, director, genre, and studio
    query = """
    SELECT film_name AS Name, 
           film_director AS Director, 
           genre_name AS Genre, 
           studio_name AS 'Studio Name'
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)
    films = cursor.fetchall()

    print("\n\t-- {} --\n".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
            film[0], film[1], film[2], film[3]))

# Connect to MySQL database
db = mysql.connector.connect(
    user="root",
    password="Powerful@2025",
    host="localhost",
    database="movies"
)

cursor = db.cursor()

# Step 5: Initial film display
show_films(cursor, "DISPLAYING FILMS")

# Step 6: Insert Star Wars (assuming studio_id=2 (20th Century Fox), genre_id=1 (SciFi))
cursor.execute("""
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES (%s, %s, %s, %s, %s, %s)
""", ("Star Wars", "1977", 121, "George Lucas", 2, 1))
db.commit()

# Step 7: Show films after insert
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Step 8: Update Alien to Horror (genre_id=3 assumed for Horror)
cursor.execute("""
    UPDATE film SET genre_id = 3 WHERE film_name = 'Alien';
""")
db.commit()

# Step 9: Show films after update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

# Step 10: Delete Gladiator
cursor.execute("""
    DELETE FROM film WHERE film_name = 'Gladiator';
""")
db.commit()

# Step 11: Show films after delete
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Clean up
cursor.close()
db.close()

