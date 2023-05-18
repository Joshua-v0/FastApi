from typing import Union
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema
from app.model import PostSchema, userSchema, userLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import  JWTBearer


posts = [
    {
     "id":1,
     "nombre":"Pan Bimbo",
     "codigo":"c723dd2163d6213"
    },
    {
     "id":2,
     "nombre":"Carne",
     "codigo":"f213123dqs3kjk"
    },

    {
     "id":3,
     "nombre":"Helado Nevada",
     "codigo":"dalsdas124312"
    }
]


users=[]


app = FastAPI()

# 1- INDEX
@app.get("/")
def read_root():
    return {"Hello": "World"}


# 2- Buscar todos los productos
@app.get("/productos", tags=["productos"])
def get_productos():
    return{"data": posts}


# 3- Buscar producto por ID 
@app.get("/productos/{id}", tags=[posts])
def get_producto_individual(id : int):
    if id > len(posts):
        return{
            "error":"No existe un producto con ese ID!"
        }
    for post in posts:
        if post["id"] == id:
            return{
                "data":post
            }

# 4- añadir un producto 
@app.post("/productos",dependencies=[Depends(JWTBearer())], tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info": "Post added."
    }


# 5- Registrar usuario [crear nuevo usuario]
@app.post("/user/signup", tags=["user"])
def user_signup(user: userSchema =Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: userLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False 
    

# 6 ruta de login 

@app.post("/user/login", tags=["user"])
def user_login(user: userLoginSchema=Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return{
            "error":"contraseña o correo incorrectos!"
        }