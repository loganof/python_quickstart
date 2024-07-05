class Counter:
    # 存储创建的对象数量
    count = 0

    def __init__(self):
        self.value = Counter.count
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


counter1 = Counter()
counter2 = Counter()
print(counter1.value)
print(counter2.value)
print(Counter.get_count())