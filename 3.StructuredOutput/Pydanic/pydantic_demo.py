from pydantic import BaseModel,Field
from typing import Optional


class Student(BaseModel):
    name: str
    batch: str = "F-23"
    age: Optional[int] = None
    cgpa:float=Field(gt=0,le=4,default=3.15,description="This is CGPA of this student.")
    # email: EmailStr  # Enforcing email format validation

new_student = {'name': 'abdul', 'age': 23,'cgpa':4}  # Valid email

student = Student(**new_student)
student_dict=dict(student)
print(student_dict)
# print(student_dict['cgpa']+"| Converted into dictionary")
print(f"{student_dict['cgpa']} | Converted into dictionary")
student_json=student.model_dump_json()
print(student_json)
print(f"{student_dict['cgpa']} | Converted into Json")
