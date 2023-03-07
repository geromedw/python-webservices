from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/surveys",response_model=schemas.Survey)
def create_survey(survey: schemas.Surveycreate,db:Session =Depends(get_db)):
    return crud.create_survey(db=db,survey=survey)

@app.post("/surveys/{survey_id}/vragen",response_model=schemas.Vraag)
def create_item_survey(survey_id:int,vraag:schemas.Vraagcreate,db:Session = Depends(get_db)):
    return crud.create_vraag(db=db,vraag=vraag,survey_id=survey_id)

@app.get("/surveys/{survey_id}",response_model=schemas.Survey)
def read_survey_by_id(survey_id:int, db:Session=Depends(get_db)):
    db_survey=crud.get_survey_by_id(db=db,survey_id=survey_id)
    return db_survey