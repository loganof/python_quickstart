"""

"""

from pydantic import BaseModel, field_serializer
from typing import Set


class StudentModel(BaseModel):
    name: str = "Jane"
    courses: Set[str]

    @field_serializer("courses", when_used="json")
    def serialize_courses_in_order(courses: Set[str]):
        return sorted(courses)


student = StudentModel(courses={"Math", "Chemistry", "English"})
print(student.model_dump_json())
