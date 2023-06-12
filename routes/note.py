from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Request
from jinja2 import Template
from fastapi.staticfiles import StaticFiles
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.FastAPI_NotesAPP.FastAPI_NotesAPP.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important":doc["important"],
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict ["important"] = True if  formDict.get("important") == "on" else False
    note = conn.FastAPI_NotesAPP.FastAPI_NotesAPP.insert_one(formDict)
    return {"Success": True}