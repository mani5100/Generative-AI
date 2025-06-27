from typing import TypedDict
class Person(TypedDict):
    name:str
    age:int
abdul :Person={
    'name':"abdul",
    'age':22
}

print(abdul)