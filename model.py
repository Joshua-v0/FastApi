from pydantic import BaseModel, Field, EmailStr


# 1- Schema para hacer un post de un producto 
class PostSchema(BaseModel):
    id : int = Field(default=None)
    nombre: str = Field(default=None)
    codigo: str = Field(default=None)
    class Config:
        schema_extra = {
            "post_demo" :{
                "nombre":"Leche chiricana ",
                "código":"c624312c16bd21"
            }
        }


# 2 schema para registrar un usuario 
class userSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default = None)
    password : str = Field(default = None)
    class Config:
        the_schema = {
            "user_demo":{
                "name" : "Joshua Voltier",
                "email" : "joshua.voltier@uip.edu.pa",
                "password" : "uip.2023"
            }
        }

# 3 schma para iniciar sesion 
class userLoginSchema(BaseModel):
    email : EmailStr = Field(default = None)
    password : str = Field(default = None)
    class Config:
        the_schema = {
            "user_demo":{
                "email" : "joshua.voltier@uip.edu.pa",
                "password" : "uip.2023"
            }
        }
            

