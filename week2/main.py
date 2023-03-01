from fastapi import FastAPI
app = FastAPI()

cars = {"merk"}

@app.get("/") # belangrijk: de path operation decorator
async def root() -> dict:
    return {"boodschap": "Hallo studenten van Web Services Python :-)"}

""" @app.get("/boodschap")
async def readboodschap(boodshap):
    return {"boodschap":boodshap} """