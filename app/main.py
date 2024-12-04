from fastapi import FastAPI
from app.routes import temperature

app = FastAPI()

# Include the temperature route
app.include_router(temperature.router)
