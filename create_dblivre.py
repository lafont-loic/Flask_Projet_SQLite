import sqlite3

connection = sqlite3.connect('database.db')

# Assurez-vous que votre fichier schema.sql crée une table 'livres' 
# avec les colonnes : titre, auteur, genre
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insertion des livres (Titre, Auteur, Genre)
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)", ('Le Petit Prince', 'Antoine de Saint-Exupéry', 'Conte'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)", ('1984', 'George Orwell', 'Dystopie'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)", ('Le Seigneur des Anneaux', 'J.R.R. Tolkien', 'Fantasy'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)", ('L''Étranger', 'Albert Camus', 'Philosophie'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)", ('Vingt mille lieues sous les mers', 'Jules Verne', 'Aventure'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)", ('Les Misérables', 'Victor Hugo', 'Roman historique'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)", ('Fondation', 'Isaac Asimov', 'Science-Fiction'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)", ('Au bonheur des dames', 'Émile Zola', 'Naturalisme'))

connection.commit()
connection.close()
