from fastapi import FastAPI

from app.database import Base, engine
from app.models import Item
from app.routes.items import router as items_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cloud Native GitOps Platform",
    version="0.2.0",
)

app.include_router(items_router)


@app.get("/")
def root():
    return {
        "application": "Cloud Native GitOps Platform",
        "version": "0.2.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    return {"status": "ready"}