from sqlmodel import Field, SQLModel
from datetime import datetime,time

class Score(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    player: str
    score: int
    level: int
    time_play: datetime  
    time_finish: time