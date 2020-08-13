from fastapi import FastAPI
import psutil

app = FastAPI()

#for test

@app.get("/")
async def root():
    return psutil.virtual_memory()