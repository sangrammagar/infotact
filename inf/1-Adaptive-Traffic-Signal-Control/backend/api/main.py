from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import random

app = FastAPI(title="Adaptive Traffic API")

class Status(BaseModel):
    queue: dict
    current_green: str
    avg_wait_time: float

@app.get("/status", response_model=Status)
def get_status():
    # Placeholder synthetic status. Replace with SUMO Traci integration.
    q = {"north": random.randint(0,20),
         "south": random.randint(0,20),
         "east": random.randint(0,20),
         "west": random.randint(0,20)}
    return Status(queue=q, current_green="north_south", avg_wait_time=round(random.random()*30,2))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
