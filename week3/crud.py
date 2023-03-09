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
    print(vraag)
    db_vraag=models.Vraag(**vraag.dict(),survey_id=survey_id)
    db.add(db_vraag)
    db.commit()
    db.refresh(db_vraag)
    return db_vraag

def get_vraag_by_id(db:Session,vraag_id:int):
    return db.query(models.Vraag).filter(models.Vraag.id == vraag_id).first()

def get_surveys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Survey).offset(skip).limit(limit).all()

def create_antwoord(db:Session,antwoord=str,vraag_id=int):
    db_antwoord=models.Antwoord(**antwoord.dict(),vraag_id=vraag_id)
    db.add(db_antwoord)
    db.commit()
    db.refresh(db_antwoord)
    return db_antwoord

def post_form(db:Session,antwoord:schemas.Antwoordcreate,vraag_id=int):
    print(antwoord)
    db_antwoord=models.Antwoord(antwoord=antwoord,vraag_id=vraag_id)
    db.add(db_antwoord)
    db.commit()
    db.refresh(db_antwoord)
    return db_antwoord   
