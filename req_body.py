# from fastapi import FastAPI
# from pydantic import BaseModel
# from model import products


# class Items(BaseModel):
#     name : str
#     des : str | None = None
#     price : int
#     tax : int


# app = FastAPI()

# @app.post("/items")
# async def read_item(item: Items):
#     return item


# @app.put("/product")
# async def getitem(product: products):
#     return product.product_name

# from typing import Annotated
# from fastapi import FastAPI, Path, Query

# app = FastAPI()

# @app.get("/item/{item_id}")

# async def read_items( item_id : Annotated[int, Path(title='The id of the item to get')], q: Annotated[str |None, Query(alias="Item Query")] =None):
#     result = {"item_id": item_id}
#     if q:
#         result.update({"q":q})
#     return result


# from fastapi import Body, FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()

# class Items(BaseModel):
#     name : str
#     description: str| None = Field( default = None, title='this description of the item', max_length= 300)
#     price : float | None = Field( gt=0, description= 'the price must be greater than zero')
#     tax : float | None = None 



# @app.put("/item/{item_id}")
# async def update_item(item_id : int, item: Items= Body(embed=True)):
#     results= {"item_id": item_id, "item":item  }
#     return results
 

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# class User(BaseModel):
#     username: str
#     full_name: str | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results



# from typing import List, Union
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     decscription : Union[str, None] = None 
#     price : float
#     tax : Union[int, None] = None
#     tag : List[str] = []

# @app.put("/item/{item_id}")
# async def update_item( item_id: int, item: Item):
#     result = {"item_id": item_id, "item": item}
#     return result


# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Image(BaseModel):
#     url: str
#     name: str


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     image: Image | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results



# from datetime import datetime, time, timedelta
# from uuid import UUID

# from fastapi import Body, FastAPI

# app = FastAPI()


# @app.put("/items/{item_id}")
# async def read_items(
#     item_id: UUID,
#     start_datetime: datetime = Body(),
#     end_datetime: datetime = Body(),
#     process_after: timedelta = Body(),
#     repeat_at: time | None = Body(default=None),
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "process_after": process_after,
#         "repeat_at": repeat_at,
#         "start_process": start_process,
#         "duration": duration,
#     }



# from fastapi import Cookie, FastAPI

# app = FastAPI()


# @app.get("/items/")
# async def read_items(ads_id: str | None = Cookie(default=None)):
#     return {"ads_id": ads_id}

from enum import Enum
from fastapi import FastAPI, Path, Query, Header, Form, File, UploadFile, HTTPException
from typing import Union
from pydantic import BaseModel

class reqb(BaseModel):
    name : str
    roll_No : int
    address : str
    Cnic : int


class Receipent(str, Enum):
    HR = "Malik Nadeem"
    Manager = "Ema Joy"
    Team_lead = "Jan Loper"

class form_get(BaseModel):
    Name: str
    Branch_no: int
    employee_id : int
    sub: str
    message: str
    receipent : Receipent   








app = FastAPI()


class number(str, Enum):
    one = "one"
    Two = "two"
    Three = "three"

@app.get("/items")

async def get_item(user_agent: str| None = Header(default=None)):
    return {"user_agent" : user_agent}

@app.get("/item/{model_num}")
async def  model(model: number):
    return {model}


@app.get("/query")
async def data(name: Union[str, None]=None, roll_no: Union[str, None] = Query(default=None, min_length=6, max_length=8) ):
    var_nam= {"name": name, "roll_no": roll_no}
    return var_nam

# form
@app.post("/form/data")
async def form1(   
        Name: str = Form(...),
        Branch_no: int = Form(...),
        employee_id : int = Form(...),
        sub: str = Form(...),
        message: str = Form(...),
        receipent : Receipent = Form(...), ):
        
        form_data = form_get  (Name=Name,
        Branch_no=Branch_no,
        employee_id=employee_id,
        sub=sub,
        message=message,
        receipent=receipent)
        return {"data": form_data}


# File
@app.post("/file/upload")
async def upload_file(file: bytes = File()):
     return ({"file": len(file)})

# UploadFile

@app.post("/upload/file")
async def file_upload(file: UploadFile):
     return({"file_name": file.filename, "file_content_type": file.content_type, "file_size": file.size})

#  UploadFile, File, Name
@app.post("/load/form")
async def form(file : UploadFile, file2: bytes = File(), name: str = Form()):
     return ({"File" : file, "file_size": file.size, "file_content_type": file.content_type, "file length": len(file2), "name": name })
# error Handling  
@app.get("/error/handling")
async def error_handling( item : int):
     if item == 2:
          return HTTPException(status_code= 400, detail="item is not equal to 2 try another value")
     return{"value": item}