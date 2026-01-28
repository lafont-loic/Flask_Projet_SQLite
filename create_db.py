import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# --- Ajout des Clients (Ton code existant) ---
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('TREMBLAY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('GAGNON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))

# --- Ajout des Livres (Même style) ---
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)",('Le Petit Prince', 'Antoine de Saint-Exupéry', 'Conte'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)",('1984', 'George Orwell', 'Dystopie'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)",('Le Seigneur des Anneaux', 'J.R.R. Tolkien', 'Fantasy'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)",('L''Étranger', 'Albert Camus', 'Philosophie'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)",('Vingt mille lieues sous les mers', 'Jules Verne', 'Aventure'))
cur.execute("INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)",('Les Misérables', 'Victor Hugo', 'Roman historique'))

# --- Ajout des Emprunts (Même style - Liaison par ID) ---
# Le 1er chiffre est l'ID du Client, le 2ème est l'ID du Livre
cur.execute("INSERT INTO emprunts (id_client, id_livre) VALUES (?, ?)",(1, 2))
cur.execute("INSERT INTO emprunts (id_client, id_livre) VALUES (?, ?)",(3, 1))
cur.execute("INSERT INTO emprunts (id_client, id_livre) VALUES (?, ?)",(8, 5))
cur.execute("INSERT INTO emprunts (id_client, id_livre) VALUES (?, ?)",(2, 3))

connection.commit()
connection.close()
