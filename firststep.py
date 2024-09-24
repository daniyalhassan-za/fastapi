# from fastapi import FastAPI
# from enum import Enum

# app = FastAPI()


# @app.get("/")

# async def root():
#     return {"mesage" : "Hello World"}


# # path parameter


# @app.get("/items/{item_id}")
# async def read_items(item_id : int):
#     return{"item_id" :item_id}

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]


# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}



# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

#Query Parameter

from typing import Optional, Annotated, Union
from fastapi import FastAPI, Query

app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]





# @app.get("/items/{item_id}")
# async def read_ittem(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}



# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item




# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item



@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


@app.get("/itoms/")
async def road_items(q: str | None = Query(default=None,  max_length = 50 )):
    results =  {"itoms": [{"item_id": "foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q" : q})
        return results
    
@app.get("/itemms")
async def read_itemms(q : Annotated[str, Query( min_length=3)] = ...):
    results = {"itemms" : [{"item_id": "foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
        return results
    

@app.get("/items/")
async def read_items(q: Annotated[Union[str, None], Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/itemms/")
async def reead_items(q : Annotated[list[str] | None , Query()] = None):
    query_items = {"q" : q}
    return query_items


@app.get("/query-items/")
async def query_items(q: Annotated[list[str], Query()] = ["", ""]):
    query_item = {"q" : q}
    return query_item

@app.get("/data/")
async def metadata( q: Annotated[str | None, Query(title= "this is Title",  min_length= 5)] = None,):
    results = {"Query_items": [{"item_id" : "foo"}, {"item_id" : "Bar"}]}

    if q:
        results.update({"q": q})
        return results
    

@app.get("/items/")
async def  reeead_items(q: Annotated[str| None, Query(title= "this is title", description="Query string for the items to search in the database that have a good match", min_length= 3)] = None):
    results = {"items" : [{"item_id" : "foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q" : q})
        return results
    
@app.get("/alias/")
async def alias_items(q : Annotated[str| None,  Query(alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,)] = None):
    results = {"items" : [{"item_id" : "foo"}, {"item_id" : "Bar"}]}
    if q:
        results.update({"q" : q})
        return results
    

@app.get("/hidquery/")
async def hidquery_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
    
