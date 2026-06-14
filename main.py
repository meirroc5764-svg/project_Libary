from fastapi import FastAPI
import uvicorn

from routes.book_routes import router as book_routes

app = FastAPI()

app.include_router(book_routes)



if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)