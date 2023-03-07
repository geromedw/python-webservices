from sqlalchemy.orm import Session
import models, schemas

def get_survey_by_id(db:Session, survey_id:int):
    return db.query(models.Survey).filter(models.Survey.id == survey_id).first()

def create_survey(db:Session, survey=schemas.Surveycreate):
    db_survey = models.Survey(title=survey.title,discription=survey.discription)
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

def create_vraag(db:Session,vraag:schemas.Vraagcreate, survey_id:int):
    db_vraag=models.Vraag(**vraag.dict(),survey_id=survey_id)
    db.add(db_vraag)
    db.commit()
    db.refresh(db_vraag)
    return db_vraag