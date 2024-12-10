from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Paperspace!"}

@app.get("/predict")
def predict(text: str):
    return {"input_text": text, "prediction": "dummy_prediction"}
