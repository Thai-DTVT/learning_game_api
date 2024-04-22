from fastapi import FastAPI, Depends #cai thu vien FastAPI
from sqlmodel import Session #tao va quan li phien lam viec
from game_api.database.database import  engine, create_db_and_tables #ket noi va tao bang csdl
from game_api.models.models import Score #tuong tac voi diem so
from game_api.schemas.schemas import GetTopScoreByLevelResponse, ScoreSchema #dinh nghia cau truc API

from game_api.crud import crud


#Khoi tao ung dung FastApi voi cai dat:URL va tieu de
app = FastAPI(
    docs_url="/docs",
    title="Game API",
)

def get_db():
    with Session(engine) as session:# Depends
        yield session
        
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

#tao diem so moi,sd cau truc ScoreSchema dau vao va tra ve mot ScoreSchema 

@app.post("/score/", response_model=ScoreSchema)
async def create_score(score: ScoreSchema, session=Depends(get_db)):
     return crud.create_score(score,session)

#lay diem so theo muc do
@app.get("/score/", response_model=GetTopScoreByLevelResponse)
async def get_score(level: int, limit: int = 30, session=Depends(get_db)):
    return crud.get_score(level,limit,session)

