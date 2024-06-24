from fastapi import APIRouter, HTTPException
from database import add, get, update, delete, list
from models import DistinctionModel


app = APIRouter()


@app.post('/distinctions', response_model=DistinctionModel)
async def create(distinction: DistinctionModel):
    response = await add(distinction.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong')

@app.get('/distinctions/{id}', response_model=DistinctionModel)
async def read(id: str):
    print(id)
    response = await get(id)
    if response:
        return response
    raise HTTPException(404, 'Not founded')

@app.put('/distinctions/{id}', response_model=DistinctionModel)
async def edit(id: str, distinction: DistinctionModel):
    response = await update(id, distinction)
    if response:
        return response
    raise HTTPException(404, 'Not founded')


@app.delete('/distinctions/{id}')
async def remove(id: str):
    response = await delete(id)
    if response:
        return "The distinction was succesfully deleted"
    raise HTTPException(404, 'Distinction not found')

@app.get('/distinctions')
async def index():
    response = await list()
    return response