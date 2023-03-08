from typing import List

from fastapi import Depends, FastAPI, HTTPException,Request,Form
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


""" @app.post("/surveys",response_model=schemas.Survey)
def create_survey(survey: schemas.Surveycreate,db:Session =Depends(get_db)):
    return crud.create_survey(db=db,survey=survey) """

@app.post("/surveys/{survey_id}/vragen",response_model=schemas.Vraag)
def create_item_survey(survey_id:int,vraag:schemas.Vraagcreate,db:Session = Depends(get_db)):
    return crud.create_vraag(db=db,vraag=vraag,survey_id=survey_id)

""" @app.get("/surveys/{survey_id}",response_model=schemas.Survey)
def read_survey_by_id(survey_id:int, db:Session=Depends(get_db)):
    db_survey=crud.get_survey_by_id(db=db,survey_id=survey_id)
    return db_survey
 """
@app.get("/surveys/{survey_id}", response_class=HTMLResponse)
async def read_by_id(request:Request, survey_id:int,db:Session=Depends(get_db)):
    db_survey=crud.get_survey_by_id(db=db,survey_id=survey_id)
    return templates.TemplateResponse("item.html", {"request":request,"surveytitel":db_survey.title,"vragen": db_survey.vragen})

@app.get("/surveys",response_class=HTMLResponse)
async def get_surveys(request:Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_surveys=crud.get_surveys(db=db,skip=skip, limit=limit)
    return templates.TemplateResponse("surveys.html",{"request":request,"surveys":db_surveys})

@app.post("/submitform")
async def post_form(verzendantwoord:str=Form()):
    return {"test":verzendantwoord}