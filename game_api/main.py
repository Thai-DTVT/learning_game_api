from fastapi import FastAPI #cai thu vien FastAPI
from sqlmodel import Session #tao va quan li phien lam viec
from game_api.database.database import  engine, create_db_and_tables #ket noi va tao bang csdl



from fastapi import FastAPI, Depends

from game_api.models.models import Score #tuong tac voi diem so
from game_api.schemas.schemas import GetTopScoreByLevelResponse, ScoreSchema #dinh nghia cau truc API

#Khoi tao ung dung FastApi voi cai dat:URL va tieu de
app = FastAPI(
    docs_url="/docs",
    title="Game API",
)

def get_session():
    with Session(engine) as session:# Depends
        yield session
        
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

#tao diem so moi,sd cau truc ScoreSchema dau vao va tra ve mot ScoreSchema 
@app.post("/score/", response_model=ScoreSchema)
async def create_score(score: ScoreSchema, session=Depends(get_session)):
    db_score = Score.model_validate(score)
    session.add(db_score)
    session.commit()
    session.refresh(db_score)
    return db_score

#lay diem so theo muc do
@app.get("/score/", response_model=GetTopScoreByLevelResponse)
async def get_score(level: int, limit: int = 5, session=Depends(get_session)):
    if limit > 10: #kiem tra gioi han
        limit = 10
#truy van csdl lay diem so theo muc do
    scores = (  
        session.query(Score)
        .filter(Score.level == level)
        .order_by(Score.score.desc())  # type: ignore
        .limit(limit)
        .all()
    )
    #tra ve han muc va diem so(scores)
    return {
        "limit": limit,
        "scores": scores,
    }
