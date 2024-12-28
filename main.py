from fastapi import FastAPI, Request 
from routes.member import router as member_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def book_test():
    return{
        "Message": "This is an application"
    }

@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=404,
        content={"message": "The page you are looking for does not exist."}
    )

app.include_router( member_router, prefix="/dali")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
