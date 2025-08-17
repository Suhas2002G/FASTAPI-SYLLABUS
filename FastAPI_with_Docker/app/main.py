from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def index():
    return {
        'message':'Hello from docker',
        'code': 200
    }