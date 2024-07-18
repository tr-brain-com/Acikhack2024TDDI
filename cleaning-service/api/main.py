import logging
import os
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

# CLEANING fonksiyonunun ve model dosyalarının import edilmesi
from clean import CLEANING
from model.request_model import RequestContent
from model.response_model import ResponseContent

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S', level=logging.INFO)
app = FastAPI(title="Brain Cleaning Service")

@app.on_event("startup")
def startup_event():
    logging.info("Server Running Worker PidID : {0}".format(os.getpid()))

@app.on_event("shutdown")
def shutdown_event():
    logging.info("Server Shutdown PidID : {0}".format(os.getpid()))

@app.post("/clean", response_model=ResponseContent)
def clean_text_dis(req: RequestContent):
    if len(req.text.strip()) == 0:
        return {"text": "Tanımsız metin girişi"}
    return {"text": CLEANING(req.text, req.constraction, req.stopword).clean()}

@app.get("/actuator/health")
def health_check():
    content = {
        "status": "UP"
    }
    return JSONResponse(content=content)


