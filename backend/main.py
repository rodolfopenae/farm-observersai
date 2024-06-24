from fastapi import FastAPI
from routes import app as distinctions_routes


app = FastAPI()
app.include_router(distinctions_routes)