from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Ta clé secrète

# --- 1. FONCTIONS UTILITAIRES ---

def get_db():
    """Une petite fonction pour éviter de répéter la connexion partout"""
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row # Important : permet d'appeler les colonnes par leur nom (ex: row['titre'])
    return conn

def est_authentifie():
    """Vérifie si l'admin est connecté"""
    return session.get('authentifie')

# --- 2. ROUTES PRINCIPALES (BIBLIOTHÈQUE) ---

@app.route('/')
def index():
    """Page d'accueil : Liste des livres + Recherche + Dashboard"""
    conn = get_db()
    
    # Gestion de la Recherche
    query = request.args.get('recherche')
    if query:
        sql = "SELECT * FROM livres WHERE titre LIKE ? OR auteur LIKE ?"
        livres = conn.execute(sql, ('%' + query + '%', '%' + query + '%')).fetchall()
    else:
        livres = conn.execute('SELECT * FROM livres').fetchall()
    
    conn.close()
    return render_template('index.html', livres=livres, admin=est_authentifie())

# --- 3. ROUTES AUTHENTIFICATION (Ton code conservé) ---

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Admin : admin / password
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['authentifie'] = True
            return redirect(url_for('index')) # Redirige vers la bibliothèque
        else:
            return render_template('formulaire_authentification.html', error=True)
    return render_template('formulaire_authentification.html', error=False)

@app.route('/logout')
def logout():
    session.pop('authentifie', None)
    return redirect(url_for('index'))

# --- 4. GESTION DES LIVRES (Ajout / Suppression / Emprunt) ---

@app.route('/ajouter_livre', methods=['POST'])
def ajouter_livre():
    # Protection : Seul l'admin peut ajouter
    if not est_authentifie():
        return redirect(url_for('authentification'))

    titre = request.form['titre']
    auteur = request.form['auteur']
    genre = request.form['genre']

    conn = get_db()
    conn.execute('INSERT INTO livres (titre, auteur, genre) VALUES (?, ?, ?)', (titre, auteur, genre))
