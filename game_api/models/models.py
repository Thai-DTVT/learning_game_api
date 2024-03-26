from sqlmodel import Field, SQLModel

class Score(SQLModel, table=True): #tao bang du lieu voi kem bang SQLModel 
    id: int = Field(default=None, primary_key=True)
    player: str
    score: int
    level: int
