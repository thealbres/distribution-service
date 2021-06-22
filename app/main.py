from fastapi import FastAPI
from .routers import calculations

app = FastAPI(title="Desafio - Distribuição dos Lucros")
app.include_router(calculations.router)

