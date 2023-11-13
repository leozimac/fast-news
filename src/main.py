from fastapi import FastAPI
from pydantic import BaseModel
import socket

app = FastAPI()

class Newsdto(BaseModel):
    title: str
    description: str
    hostname: str

class News(BaseModel):
    id: int
    title: str
    description: str

news_list = [News(id=1, title= "Kubernetes e alta disponibilidade", description="Kubernetes é uma ferramente open source que nos traz..."),
             News(id=2, title="Docker e containers", description="Com Docker e containers, conseguimos trazer..."),
             News(id=3, title="IAC com Terraform", description="Podemos automatizar e versionar a criação da nossa infra com Terraform..."),
             News(id=4, title="Gerênciamento de ambiente com Ansible", description="Ansible automatiza o gerênciamento de sistemas remotes e controla..."),]

@app.get("/news")
async def all_news():
    return {"news": news_list}

@app.get("/news/{news_id}")
async def news(news_id: int):
    for item in news_list:
        if item.id == news_id:
            story = item

    response = Newsdto(title=story.title, description=story.description, hostname=socket.gethostname())
    return response

@app.post("/news")
async def news(story: News):
    news_list.append(story)
    return {"message": "Story added succesfuly."}