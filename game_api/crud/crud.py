from fastapi import FastAPI, Depends #cai thu vien FastAPI
from sqlmodel import Session #tao va quan li phien lam viec
from game_api.database.database import  engine, create_db_and_tables #ket noi va tao bang csdl
from game_api.models.models import Score #tuong tac voi diem so
from game_api.schemas.schemas import GetTopScoreByLevelResponse, ScoreSchema #dinh nghia cau truc API

def create_score(score: ScoreSchema, session=Session):
    db_score = Score.model_validate(score)
    session.add(db_score)
    session.commit()
    session.refresh(db_score)
    return db_score

def get_score(level: int, limit: int = 5, session=Depends(Session)):
    if limit > 10: #kiem tra gioi han
        limit = 10
#truy van csdl lay diem so theo muc do
    scores = (  
        session.query(Score)
        .filter(Score.level == level)
        .order_by(Score.score.desc()) 
        .limit(limit)
        .all()
    )
    #tra ve han muc va diem so(scores)
    return {
        "limit": limit,
        "scores": scores,
    }
