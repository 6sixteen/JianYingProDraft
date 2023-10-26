from dataclasses import dataclass,field

@dataclass
class Person:
    name: str = field()
    age: int = field(default=1)

p = Person(1)