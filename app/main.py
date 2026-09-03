from fastapi import FastAPI

app = FastAPI(
    title="Cloud Native GitOps Platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "Cloud Native GitOps Platform",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}