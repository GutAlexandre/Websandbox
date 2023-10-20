from fastapi import FastAPI, Request, HTTPException, WebSocket, Form, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.websockets import WebSocketDisconnect
import json


app = FastAPI()
templates = Jinja2Templates(directory="web")
site_name = "Alex-website" 
app.mount("/images", StaticFiles(directory="web/images"), name="images")
app.mount("/libs", StaticFiles(directory="web/libs"), name="libs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

websocket_connections: List[WebSocket] = []
websocket_connections_name = []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    progress_bar = f'''
        <div class="progress">
            <div class="progress-bar" role="progressbar" style="width: 50%; background-color: #f9d852;"
                aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
                <span class="sr-only">50%</span>
            </div>
        </div>
    '''
    img = f'''
            <div class="image-container">
                <img src="/images/IMG_3030.jpeg" alt="Description de l'image" style="width: 50%;; display: block; margin: 0 auto;">
            </div>
            '''
    cards = [
        {"color": "#215577", "title": "Envoyer l'image à l'écran", "text": progress_bar, "button":"true", "button_text":"Go","href":""},
        {"color": "#217777", "title": "Envoyer l'image à l'écran", "text": img, "button":"true", "button_text":"Go","href":""},
        {"color": "#218877", "title": "Envoyer l'image à l'écran", "text": "This card has supporting text below as a natural lead-in to additional content.", "button":"true", "button_text":"Go","href":""},
        {"color": "#212e77", "title": "Envoyer l'image à l'écran", "text": "This card has supporting text below as a natural lead-in to additional content.", "button":"false", "button_text":"Go","href":""},
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
    

    disposition = [2,2]
    num_rows = len(disposition)
    total_elements = len(cards)

    if sum(disposition) != total_elements:
        raise ValueError("La somme de la disposition des éléments ne correspond pas au nombre total d'éléments.")

    index = 0
    data = {"title": "Accueil", "content": "Ceci est la page d'accueil.", "num_rows": num_rows,"navbar_content": navbar_content,"disposition":disposition}

    data["rows"] = []

    for row_size in disposition:
        row = []
        for _ in range(row_size):
            row.append(cards[index])
            index += 1
        data["rows"].append(row)

    # data = {"title": "Accueil", "content": "Ceci est la page d'accueil.", "cards": cards, "num_columns": num_columns, "num_rows": num_rows,"navbar_content": navbar_content}
    return templates.TemplateResponse("templates/index.html", {"request": request, **data})



@app.get("/chatwebsocket", response_class=HTMLResponse)
async def read_page1(request: Request):
    return templates.TemplateResponse("templates/chatwebsocket.html", {"request": request })

@app.get("/get_connections", response_model=dict)
async def get_connections():
    connections = await ws_list()  
    return {"connections": connections}

@app.post("/send_message_to")
async def send_message_to(message: str = Form(...), id: str = Form(...), who: str = Form(...)):
    print(id)
    if id=='Broadcast':
        connections = await broadcast_message(message) 
    else:
        connections = await send_message_to_id(message,int(id),who) 
    return {"connections": connections}



@app.websocket("/ws/{pseudo}")
async def websocket_endpoint(websocket: WebSocket, pseudo: str):
    await websocket.accept()    
    websocket_connections.append(websocket)
    websocket_connections_name.append(pseudo)
    try:
        while True:
            data = await websocket.receive_text()

            connections = [str(connection) for connection in websocket_connections]
            elements = data.split('&')
            data_dict = {}
            for element in elements:
                key, value = element.split('=')
                if '?' in key:
                    url, key = key.split('?', 1)

                value = value.replace('%28', '(') 
                data_dict[key] = value

            if data_dict['id'] in websocket_connections_name:
                index = websocket_connections_name.index(data_dict['id'])
                data_dict['id'] = index


            print(data_dict)
            if data_dict['id']=='Broadcast':
                connections = await broadcast_message(data_dict['message']) 
            else:
                connections = await send_message_to_id(data_dict['message'],int(data_dict['id']),data_dict['who']) 
            # await websocket.send_json({"connections": connections})


            # await websocket.send_text(f"Message text was: {data}")
            # await broadcast_message(data)
    except WebSocketDisconnect:
        index = websocket_connections.index(websocket)
        websocket_connections_name.pop(index)
        websocket_connections.remove(websocket)
        

async def ws_list():
    connections = [str(connection) for connection in websocket_connections_name]
    return {"connections": connections}

async def broadcast_message(message: str):
    for connection in websocket_connections:
        await connection.send_text(message)

# async def send_message_to_id(message: str,index: int,who:str):
#     message = who + " say : " + message
#     await websocket_connections[index].send_text(message)

async def send_message_to_id(message, index, who):
    message = who + " say : " + message
    if 0 <= index < len(websocket_connections):
        try:
            await websocket_connections[index].send_text(message)
        except WebSocketDisconnect:
            print("WebSocket connection closed.")
    else:
        print(f"Invalid index: {index}")


@app.get("/{path:path}", response_class=HTMLResponse)
async def not_found(request: Request):
    try:
        raise HTTPException(status_code=404, detail="Page not found")
    except HTTPException as exc:
        error_code = exc.status_code
    
    data = {"title": "Erreur " + str(error_code),"status_code":error_code}
    return templates.TemplateResponse("templates/Error_page.html", {"request": request, **data})



