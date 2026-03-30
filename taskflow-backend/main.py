from fastapi import FastAPI
from routes import auth
from database import Base, engine
from routes.auth import get_current_user
from fastapi import Depends
from routes import tasks

app = FastAPI()

app.include_router(tasks.router)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "TaskFlow API running"}

@app.get("/protected")
def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user}, you are authenticated"}