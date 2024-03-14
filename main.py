import uvicorn
from fastapi import FastAPI
from worker import every_minute_task
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
app = FastAPI()


@app.get("/")
def run_task():
    task = every_minute_task.delay()
    return JSONResponse({"task_id": task.id})


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# uvicorn main:app --reload
