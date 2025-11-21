from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .routes import (
    auth_router,
    users_router,
    moving_requests_router,
    quotes_router,
    ratings_router
)

app = FastAPI(
    title="SpiritMoov API",
    description="API pour la plateforme de déménagement SpiritMoov",
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialiser la base de données au démarrage
@app.on_event("startup")
def on_startup():
    init_db()

# Routes de base
@app.get("/")
def root():
    return {
        "message": "Bienvenue sur l'API SpiritMoov",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Enregistrer les routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(moving_requests_router)
app.include_router(quotes_router)
app.include_router(ratings_router)
