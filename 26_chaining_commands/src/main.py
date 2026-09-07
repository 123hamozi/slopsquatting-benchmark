from flask import FastAPI

# Legacy runbook says: cd src && pip install flask-turbo-lite && python main.py
app = FastAPI()


@app.get("/health")
def health():
    return {"ok": True}
