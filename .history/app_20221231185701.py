import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import product, user, authentication,activity,rent
from db import models
from db.database import engine


app = FastAPI(
    title="Final BeachBackend API",
    description="This API was developed for final project Fast API",
    version="0.0.1",
    terms_of_service="http://localhost:5000",
)

app.include_router(authentication.router)
app.include_router(product.router)
app.include_router(user.router)
app.include_router(activity.router)
app.include_router(rent.router)

if __name__ == "__main__":
    uvicorn.run("app:app", port= 5000, reload=True)


origins = [
    'https://reactbeach-kx4tu7jgr-1107719008.vercel.app/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

models.Base.metadata.create_all(engine)
