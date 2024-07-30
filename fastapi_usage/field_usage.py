"""
Field 是pydantic模块中的一个函数, 用于pydantic模型中设置字段默认值、别名、验证规则和提供描述等。
"""

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(
        ..., alias="user_id", description="The unique identifier of the user"
    )
    name: str = Field(..., max_length=50, description="The name of the user")
    age: int = Field(0, gt=0, description="The age of the user, must be greater than 0")


user = User(user_id=1, name="Alice", age=25)
print(user)
