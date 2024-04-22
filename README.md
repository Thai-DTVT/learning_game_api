#FastAPI with SQLModel use SQLite
- Use poetry install the packages


`uvicorn --app-dir=. game_api.main:app --reload`
`docker build -t game_api/mycontainer .`
`docker run -d -p 80:80 game_api/mycontainer`
`docker login`
`docker push thaipham98/game_api:latest`