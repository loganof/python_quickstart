
from typing import Iterable, Text

def process_strings(strings: Iterable[Text]) -> None:
    for string in strings:
        print(string)
        
        
process_strings(["hello", "world"])
process_strings(("hello", "world"))
process_strings(set(["hello", "world"]))