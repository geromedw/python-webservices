from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Survey(Base):
    __tablename__ = "surveys"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=False, index=True)
    discription = Column(String, unique=False, index=True)

    vragen=relationship("Vraag",back_populates="survey")

class Antwoord(Base):
    __tablename__ = "antwoorden"
    id = Column(Integer,primary_key=True,index=True)
    antwoord=Column(String,unique=False,index=True)
    vraag_id = Column(Integer,ForeignKey("vragen.id"))
    vraag_vraag=relationship("Vraag",back_populates="antwoorden")


class Vraag(Base):
    __tablename__ = "vragen"
    id = Column(Integer, primary_key=True, index=True)
    vraag = Column(String, unique=False, index=True)
    survey_id=Column(Integer, ForeignKey("surveys.id"))
    survey = relationship("Survey",back_populates="vragen")
    antwoorden = relationship("Antwoord", back_populates="vraag_vraag")
