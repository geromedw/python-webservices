from pydantic import BaseModel

class Antwoordbase(BaseModel):
    antwoord:str

class Antwoordcreate(Antwoordbase):
    pass

class Antwoord(Antwoordbase):
    id:int
    vraag_id:int
    class Config:
        orm_mode = True


class Vraagbase(BaseModel):
    vraag : str

class Vraagcreate(Vraagbase):
    pass

class Vraag(Vraagbase):
    id:int
    survey_id:int
    antwoorden: list[Antwoord] = []
    class Config:
        orm_mode = True


class Surveybase(BaseModel):
    title: str
    discription : str

class Surveycreate(Surveybase):
    pass

class Survey(Surveybase):
    id:int
    vragen: list[Vraag] = []

    class Config:
        orm_mode = True


