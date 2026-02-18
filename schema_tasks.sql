DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    description TEXT,
    date_echeance TEXT,
    termine INTEGER DEFAULT 0 -- 0 = En cours, 1 = Terminé
);
