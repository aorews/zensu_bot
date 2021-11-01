import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello from Zensu!'}


if __name__ == '__main__':
    uvicorn.run('example:app', host='127.0.0.1', port=5000, log_level='info')
