使用pydantic的BaseModel
1. 自动验证数据
2. 自动转化错误类型的数据
   1. 如果参数类型为int,传入时为string，能够自动转化
3. 内置了序列化与反序列化
   1. 序列化：myClass.json()
   2. 反序列化:myClass.dict()
   3. 我们需要搞清楚序列化与反序列化的概念：
      1. 序列化：将对象转换成一个可存储或可传输的格式，如json,xml,yaml,二进制等。
         1. 在python中，json.dumps()
      2. 反序列化：将字符串、字节流等格式还原为对象。
         1. 在python中，json.loads()
4. 支持嵌套模型和复杂的数据结构
5. 默认装饰器@validator,@root_validator等数据验证