from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import appointments, clients_pets, inventory, forecast, analytics


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost:3000", "http://localhost:5173", "https://front-univet2-p3vk0ced6-matheus-limas-projects-90388d72.vercel.app", "https://front-univet-wnka.vercel.app", "https://front-univet-wnka-git-main-matheus-limas-projects-90388d72.vercel.app", "https://front-univet-wnka-ty9tz30cx-matheus-limas-projects-90388d72.vercel.app", "https://front-univet2.vercel.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(appointments.router)
app.include_router(clients_pets.router)
app.include_router(inventory.router)
app.include_router(forecast.router)


