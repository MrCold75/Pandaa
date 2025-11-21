# 🚚 SpiritMoov - Application de Déménagement

**SpiritMoov** est une plateforme web moderne qui connecte les clients avec des déménageurs professionnels. Inspirée du modèle du Bon Coin, elle offre un système de notation transparent et une gestion complète des déménagements.

-----

## 🎯 Fonctionnalités

### Pour les Clients

- ✅ Créer des demandes de déménagement (point A → point B)
- 📸 Ajouter des photos des objets à déménager
- 💰 Recevoir et comparer plusieurs devis
- ⭐ Noter les déménageurs après le service
- 💬 Communiquer directement avec les déménageurs

### Pour les Déménageurs

- 🏢 Créer un profil professionnel complet
- 📋 Consulter les demandes disponibles dans leur zone
- 📝 Envoyer des devis personnalisés
- ⭐ Construire leur réputation via les notations
- 📊 Gérer leurs missions et disponibilités

-----

## 🛠️ Technologies utilisées

### Backend

- **Python 3.10+** - Langage principal
- **FastAPI** - Framework web moderne et rapide
- **SQLAlchemy** - ORM pour la base de données
- **SQLite** (dev) / **PostgreSQL** (production)
- **Pydantic** - Validation des données
- **JWT** - Authentification sécurisée

### Frontend

- **React 18** - Bibliothèque UI
- **Vite** - Build tool ultra-rapide
- **Tailwind CSS** - Framework CSS moderne
- **Axios** - Client HTTP
- **React Router** - Navigation
- **React Hook Form** - Gestion des formulaires

### DevOps

- **Docker** - Conteneurisation
- **GitHub Actions** - CI/CD
- **Vercel** - Hébergement frontend
- **Render/Railway** - Hébergement backend

-----

## 🚀 Installation et démarrage

### Prérequis

- Python 3.10 ou supérieur
- Node.js 18 ou supérieur
- Git

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/MrCold75/Pandaa.git
cd Pandaa
```

### 2️⃣ Configuration Backend

```bash
# Aller dans le dossier backend
cd backend

# Créer un environnement virtuel Python
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows:
venv\Scripts\activate
# Sur Mac/Linux:
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Copier le fichier d'environnement
cp .env.example .env

# Lancer le serveur de développement
uvicorn app.main:app --reload
```

Le backend sera accessible sur `http://localhost:8000`
Documentation API Swagger: `http://localhost:8000/docs`

### 3️⃣ Configuration Frontend

Ouvrir un nouveau terminal :

```bash
# Aller dans le dossier frontend
cd frontend

# Installer les dépendances
npm install

# Copier le fichier d'environnement
cp .env.example .env

# Lancer le serveur de développement
npm run dev
```

Le frontend sera accessible sur `http://localhost:5173`

-----

## 🐳 Démarrage avec Docker (Optionnel)

```bash
# À la racine du projet
docker-compose up -d
```

Tout sera lancé automatiquement :

- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`

-----

## 📖 Documentation API

La documentation interactive de l'API est disponible à :

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Endpoints principaux

#### Authentification

- `POST /api/auth/register` - Inscription
- `POST /api/auth/login` - Connexion

#### Utilisateurs

- `GET /api/users/me` - Profil actuel
- `PUT /api/users/me` - Mettre à jour le profil
- `GET /api/users/{id}` - Profil public d'un utilisateur

#### Demandes de déménagement

- `POST /api/moving-requests` - Créer une demande
- `GET /api/moving-requests` - Liste des demandes
- `GET /api/moving-requests/{id}` - Détails d'une demande
- `PUT /api/moving-requests/{id}` - Modifier une demande
- `DELETE /api/moving-requests/{id}` - Supprimer une demande

#### Devis

- `POST /api/quotes` - Créer un devis
- `GET /api/quotes` - Liste des devis
- `GET /api/quotes/{id}` - Détails d'un devis
- `PUT /api/quotes/{id}/accept` - Accepter un devis
- `PUT /api/quotes/{id}/reject` - Refuser un devis

#### Notations

- `POST /api/ratings` - Créer une notation
- `GET /api/ratings/user/{id}` - Notations d'un utilisateur

-----

## 🎨 Palette de couleurs

```css
/* Couleurs principales */
--primary-blue: #2563EB;      /* Bleu électrique */
--secondary-orange: #F97316;   /* Orange vif */
--success-green: #10B981;      /* Vert succès */
--neutral-gray: #64748B;       /* Gris moderne */

/* Couleurs de fond */
--bg-light: #F8FAFC;
--bg-white: #FFFFFF;
--bg-dark: #1E293B;
```

-----

## 📁 Structure du projet

```
Pandaa/
├── backend/                    # API Python FastAPI
│   ├── app/
│   │   ├── main.py            # Point d'entrée de l'API
│   │   ├── database.py        # Configuration base de données
│   │   ├── models/            # Modèles SQLAlchemy
│   │   ├── schemas/           # Schémas Pydantic
│   │   ├── routes/            # Routes API
│   │   └── utils/             # Utilitaires
│   ├── requirements.txt       # Dépendances Python
│   ├── .env.example          # Variables d'environnement exemple
│   └── Dockerfile            # Configuration Docker
│
├── frontend/                  # Application React
│   ├── src/
│   │   ├── components/       # Composants réutilisables
│   │   ├── pages/            # Pages de l'application
│   │   ├── services/         # Services API
│   │   ├── context/          # Context API React
│   │   ├── App.jsx           # Composant principal
│   │   └── main.jsx          # Point d'entrée
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── .env.example
│
├── docker-compose.yml         # Configuration Docker Compose
├── .gitignore
└── README.md                  # Ce fichier
```

-----

## 🤝 Contribution

### Workflow Git

1. **Créer une branche** pour votre fonctionnalité

```bash
git checkout -b feature/nom-fonctionnalite
```

2. **Faire vos modifications** et commiter

```bash
git add .
git commit -m "feat: description de la fonctionnalité"
```

3. **Pousser la branche**

```bash
git push origin feature/nom-fonctionnalite
```

4. **Créer une Pull Request** sur GitHub

### Convention de commit

- `feat:` Nouvelle fonctionnalité
- `fix:` Correction de bug
- `docs:` Documentation
- `style:` Formatage
- `refactor:` Refactorisation
- `test:` Ajout de tests
- `chore:` Tâches de maintenance

-----

## 📝 Variables d'environnement

### Backend (.env)

```env
DATABASE_URL=sqlite:///./spiritmoov.db
SECRET_KEY=votre-cle-secrete-super-longue-et-aleatoire
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env)

```env
VITE_API_URL=http://localhost:8000/api
VITE_APP_NAME=SpiritMoov
```

-----

## 📄 Licence

MIT License - Ce projet est open source et libre d'utilisation.

-----

## 👥 Auteurs

Développé avec ❤️ par l'équipe SpiritMoov
