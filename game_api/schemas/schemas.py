from pydantic import BaseModel
from datetime import datetime,time

class ScoreSchema(BaseModel): 
    player: str
    score: int
    level: int
    time_play: datetime = datetime.now()
    time_finish: time = datetime.now().time()
class GetTopScoreByLevelResponse(BaseModel): 
    limit: int
    scores: list[ScoreSchema] = []

