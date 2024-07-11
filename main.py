from fastapi import FastAPI, HTTPException
import uvicorn

from ramos_direito.routers import ramos_direito_router

app = FastAPI()


@app.get("/")
def primeira_pagina():
    return {"message": "Previsao das peças"}


app.include_router(ramos_direito_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
