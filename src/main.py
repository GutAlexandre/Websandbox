from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="web")
site_name = "Alex-website" 

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    cards = [
        {"color": "#215577", "title": "Envoyer l'image à l'écran", "text": "This card has supporting text below as a natural lead-in to additional content.", "button":"true"},
        {"color": "#217777", "title": "Envoyer l'image à l'écran", "text": "This card has supporting text below as a natural lead-in to additional content.", "button":"true"},
        {"color": "#218877", "title": "Envoyer l'image à l'écran", "text": "This card has supporting text below as a natural lead-in to additional content.", "button":"true"},
        {"color": "#212e77", "title": "Envoyer l'image à l'écran", "text": "This card has supporting text below as a natural lead-in to additional content.", "button":"false"},
    ]
    navbar_content = [
        {
            "type": "dropdown",
            "class": "nav-link dropdown-toggle",
            "text": "Menu principal",
            "items": [
                {"class": "dropdown-item", "text": "Sous-menu 1", "href": "#"},
                {"class": "dropdown-item", "text": "Sous-menu 2", "href": "#"},
            ],
        },
        {
            "type": "dropdown",
            "class": "nav-link dropdown-toggle",
            "text": "Autre menu",
            "items": [
                {"class": "dropdown-item", "text": "Sous-menu 3", "href": "#"},
            ],
        },
        {
            "type": "nav-link",
            "class": "nav-item",
            "text": "Autre menu",
            "href": "/paint.html",
        },
        {
            "type": "search"
        },
        {
            "type": "text",
            "text": "Texte"
        },
        {
            "type": "button",
            "class": "btn btn-danger",
            "text": "Autre menu",
            "onclick": "alert('ooo')",
        },
    ]
    num_columns = 3
    num_rows = -(-len(cards) // num_columns) 
    data = {"title": "Accueil", "content": "Ceci est la page d'accueil.", "cards": cards, "num_columns": num_columns, "num_rows": num_rows,"navbar_content": navbar_content}
    return templates.TemplateResponse("templates/index.html", {"request": request, **data})






@app.get("/page1", response_class=HTMLResponse)
async def read_page1(request: Request):
    data = {"title": "Page 1", "content": "Ceci est la page 1."}
    return templates.TemplateResponse("templates/index.html", {"request": request, **data})

@app.get("/page2", response_class=HTMLResponse)
async def read_page2(request: Request):
    data = {"title": "Page 2", "content": "Ceci est la page 2."}
    return templates.TemplateResponse("templates/index.html", {"request": request, **data})
