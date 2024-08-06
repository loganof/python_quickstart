"""
@model_validator validate multiple parameters, supporting mode equals "before","after", "wrap"
1. mode=before:class method, recommend user @classmethod below @model_validator
2. mode=after: instance method
@root_validator has been deprecated, and should be replaced with @model_validator.
"""

from typing import Dict
from pydantic import BaseModel, Field, model_validator


def get_from_dict_or_file(values, key, file_name):
    # 示例函数实现，从字典或文件中获取值
    # 具体实现取决于你的需求
    return values.get(key, f"Default value from {file_name}")


class MyModel(BaseModel):
    sensenova_api_base: str = Field(default=None)
    completion_url: str = Field(default=None)

    @model_validator(mode="before")
    @classmethod
    def validate_environment(cls, values: Dict) -> Dict:
        values["sensenova_api_base"] = get_from_dict_or_file(
            values, "sensenova_api_base", "sensenova_chat_config.json"
        )
        values["completion_url"] = get_from_dict_or_file(
            values, "completion_url", "sensenova_chat_config.json"
        )
        return values


# 示例用法
data = {
    # 你的输入数据
}

model_instance = MyModel(sensenova_api_base="str")
print(model_instance)
