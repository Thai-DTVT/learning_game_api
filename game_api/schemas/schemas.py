from pydantic import BaseModel # thu vien pydantic Python kiem tra va validate du lieu


class ScoreSchema(BaseModel): #cau truc du lieu can co 
    player: str
    score: int
    level: int


class GetTopScoreByLevelResponse(BaseModel): #lay diem so cao nhat voi muc do
    limit: int #gioi han 
    scores: list[ScoreSchema] = [] #tra ve [] neu khong co diem