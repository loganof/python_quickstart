"""
@field_validator: class method, recommend the @classmethod decorator below the @field_validator
mode=before:
    1. 将用户输入进行格式化, 例如去除空白字符、转换大小写、解析日期字符串等。
    2. 将数据标准化，以便后续验证和处理。
mode=after:
    在数据通过验证之后进行额外的逻辑检查。
    
caveat: @validator has been deprecated, and should be replaced with @field_validator.

"""

from pydantic import BaseModel, Field, field_validator, ValidationError


class User(BaseModel):
    username: str
    email: str = Field(...)

    # 在验证前处理username 字段
    @field_validator("username", mode="before")
    @classmethod
    def nomalize_username(cls, v):
        return v.strip().lower()

    # 在验证后处理email字段
    @field_validator("email", mode="before")
    def check_email_domain(cls, v):
        if not v.endswith("@example.com"):
            raise ValueError("Invalid email domain")
        return v


# user = User(username=" Alice ", email="alice@example.com")
# print(user.username)

try:
    user = User(username="alice", email="alice@gmail.com")
except ValidationError as e:
    print(e)
