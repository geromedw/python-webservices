from sqlalchemy.orm import Session
import models, schemas

def create_car(db: Session, car: schemas.carCreate):
    db_car=models.cars(brand=car.brand, type=car.type, score=car.score)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_car_by_type(db: Session, type:str):
    return db.query(models.cars).filter(models.cars.type == type).first()

def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.cars).offset(skip).limit(limit).all()

def get_brand(db: Session, brand: str):
    return db.query(models.cars).filter_by(brand=brand).all()

def delete_type(db: Session, car: schemas.car):
    print("ok")
    db.query(models.cars).filter(models.cars.type==car.type).delete()
    db.commit()