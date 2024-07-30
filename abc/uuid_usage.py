import uuid

# uuid4
uuid4 = uuid.uuid4()
print(uuid4)

# uuid5
# 在相同的命名空间和名称下，生成的UUID是一致的，适用
namespace = uuid.NAMESPACE_DNS
name = "example.com"
uuid5 = uuid.uuid5(namespace, name)
print(uuid5)
