from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# conn = MongoClient("mongodb+srv://test1:Cluster0@@55@cluster0.erb49.mongodb.net/")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # database = conn["nodes"]
    # collection = database["notes"]
    # docs = collection.find_one({})
    # print(docs)
    return templates.TemplateResponse(request=request, name="index.html")