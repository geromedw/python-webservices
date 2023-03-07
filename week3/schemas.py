from pydantic import BaseModel

class Vraagbase(BaseModel):
    vraag : str

class Vraag(Vraagbase):
    id:int
    vraag:str
    survey_id:int
    class Config:
        orm_mode = True

class Vraagcreate(Vraagbase):
    pass


class Surveybase(BaseModel):
    title: str
    discription : str

class Surveycreate(Surveybase):
    title= str

class Survey(Surveybase):
    id:int
    title : str
    discription : str
    vragen: list[Vraag] = []

    class Config:
        orm_mode = True