import uvicorn

from bookstore.core.infrastructure.config import config

if __name__ == "__main__":
    uvicorn.run(
        "bookstore.core.infrastructure.http:app",
        host="0.0.0.0",
        port=config.API_PORT,
        reload=True,
    )
