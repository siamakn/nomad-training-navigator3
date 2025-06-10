from fastapi import FastAPI

app = FastAPI(title="NOMAD Training Metadata Manager", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Welcome to NOMAD Training Metadata Manager API"}
