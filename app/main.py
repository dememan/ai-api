from fastapi import FastAPI

app = FastAPI(title="AI API",    version="2.0.0")


@app.get("/")
def root():
    return {"message": "AI API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
