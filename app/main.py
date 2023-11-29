from fastapi import FastAPI
from app.routes import auth, sign, user, models, streaming
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(sign.router)
app.include_router(user.router)
app.include_router(models.router)
app.include_router(streaming.router)

# Instrumenta tu aplicación para exponer métricas Prometheus en /metrics
Instrumentator().instrument(app).expose(app)
##! [] crate token persistance change on login
