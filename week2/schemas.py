from pydantic import BaseModel

class carBase(BaseModel):
    brand: str
    type: str

class carCreate(carBase):
    score: int

class car(carBase):
    id: int
    brand: str
    type : str
    score : int

    class Config:
        orm_mode = True