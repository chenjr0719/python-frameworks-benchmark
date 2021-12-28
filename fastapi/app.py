import os

import databases
from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse

DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)

app = FastAPI()



@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/db", response_class=HTMLResponse)
async def handle_db():
    result = await database.fetch_val("SELECT html FROM render_cache_pagehtml WHERE url='startmatter.com'")
    return result
