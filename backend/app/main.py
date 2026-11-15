from fastapi import FastAPI

app = FastAPI(title="Frontdesk AI")


@app.get("/")
def root():
    return {"status": "ok"}
