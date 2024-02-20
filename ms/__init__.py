from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("./model/model_binary.dat.gz")
