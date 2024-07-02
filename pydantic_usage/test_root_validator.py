from pydantic import BaseModel, root_validator

class UserModel(BaseModel):
    username: str
    password: str
    password_confirm: str
    # 验证器会在字段验证之前运行，将所有字符串前后的空白字符去掉
    @root_validator(pre=True)
    def strip_whitespace(cls, values):
        values = {k: v.strip() if isinstance(v, str) else v for k, v in values.items()}
        return values
    
    @root_validator()
    def check_passwords_match(cls, values):
        password = values.get("password")
        passwork_confirm = values.get("password_confirm")
        if password != passwork_confirm:
            raise ValueError("Passwords do not match")
        return values
    
try:
    user = UserModel(username=" user1", password=" secret ", password_confirm=" secret1 ")
    print(user)
    
except ValueError as e:
    print(e)