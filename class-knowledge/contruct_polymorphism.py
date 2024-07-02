from typing import Text, Any

class InputData:
    def read(self) -> None:
        raise NotImplementedError
    
class PathInputData(InputData):
    def __init__(self, path: Text) -> None:
        super().__init__()
        self.path = path
        
    def read(self):
        with open(self.path) as f:
            return f.read()
        
        
from typing import Iterable
class Worker:
    def __init__(self, input_data: Any) -> None:
        self.input_data = input_data
        self.result = None

    def map(self)-> Iterable[Any]:
        raise NotImplementedError
    
    def reduce(self, other: "Worker") -> Any:
        raise NotImplementedError
    
    
class LineCountWorker(Worker):
    def map(self) -> Iterable[Any]:
        data = self.input_data.read()
        self.result = data.count('\n')
    
    def reduce(self, other: Worker) -> Any:
        self.result += other.result
        
import os
def generate_inputs(data_dir: Text):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))
        
from typing import List
def create_workers(input_list: List[Text]) -> List[Worker]:
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


from threading import Thread

def execute(workers: Worker) -> Any:
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    
    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result

def mapreduce(data_dir: Text) -> Any:
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)

import random
def write_test_files(tmpdir: Text):
    os.makedirs(tmpdir)
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), 'w') as f:
            f.write('\n' * random.randint(0, 100))
tmpdir = 'test_inputs'
# write_test_files(tmpdir)
result = mapreduce(tmpdir)
print(f'There are {result} lines')


from typing import Dict
class GenericInputData:
    def read(self):
        raise NotImplementedError
    
    @classmethod
    def generate_inputs(cls, config: Dict[Any, Text]):
        raise NotImplementedError
    
    
class PathInputData_V2(GenericInputData):
    def __init__(self, path: Text) -> None:
        super().__init__()
        self.path = path
        
    def read(self):
        with open(self.path) as f:
            return f.read()
        
    @classmethod
    def generate_inputs(cls, config: Dict[Any, Text]):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))
            
class GenericWorker:
    def __init__(self, input_data: Text) -> None:
        self.input_data = input_data
        self.result = None
        
    def map(self) -> Iterable[Any]:
        raise NotImplementedError
    
    def reduce(self, other: "GenericWorker") -> Any:
        raise NotImplementedError
    
    @classmethod
    def create_workers(cls, input_class: GenericInputData, config: Dict[Any, Text]) -> List[GenericInputData]:
        workers = []
        for input_data in input_class.generate_inputs(config): # polymorphism
            workers.append(cls(input_data))
        return workers
    
class LineCountWorker_V2(GenericWorker):
    def map(self) -> Iterable[Any]:
        data = self.input_data.read()
        self.result = data.count('\n')
    
    def reduce(self, other: Worker) -> Any:
        self.result += other.result
        
def mapreduce_V2(worker_class: GenericWorker, input_class: GenericInputData, config: Dict[Any, Text]) -> Any:
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


config = {'data_dir': tmpdir}
result = mapreduce_V2(LineCountWorker_V2, PathInputData_V2, config)
print(f"There are {result} lines")