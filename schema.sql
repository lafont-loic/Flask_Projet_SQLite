-- 1. On nettoie les anciennes tables pour repartir sur une base propre
DROP TABLE IF EXISTS emprunts;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS livres;

-- 2. Création de la table Client (ceux qui empruntent)
CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    adresse TEXT NOT NULL,
    role TEXT DEFAULT 'USER' -- Pour la gestion Admin/Utilisateur demandée
);

-- 3. Création de la table Livre (le stock de la bibliothèque)
CREATE TABLE livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    genre TEXT,
    stock INTEGER DEFAULT 1 -- Pour la gestion des stocks demandée
);

-- 4. Création de la table Emprunt (Le lien entre les deux)
CREATE TABLE emprunts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER NOT NULL, 
    id_livre INTEGER NOT NULL,
    date_emprunt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_retour_prevue DATE,
    -- Ces lignes créent le lien réel entre les tables
    FOREIGN KEY (id_client) REFERENCES clients (id),
    FOREIGN KEY (id_livre) REFERENCES livres (id)
);
