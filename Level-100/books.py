from fastapi import FastAPI, Query, Path


app = FastAPI()


@app.get('/')
def get_books():
    return {'welcome':'back'}


@app.get('/book_by_path/{bid}')
def get_book_by_id(
    bid:str = Path(..., description='Fetch book detail by using id')
):
    return {
        "id" : bid,
        "name" : f"start-{bid}"
    }


@app.get('/book_by_query')
def get_book(
    bid:str = Query(..., description='Fetch book detail by using id')
):
    return {
        "id" : bid,
        "name" : f"start-{bid}"
    }