from dataclasses import dataclass, field


@dataclass
class Book:
    id: int = field(init=False)
    title: str
    author: str

    __id_counter = 0 # id will be equals to created instances

    def __post_init__(self):
        Book.__id_counter += 1
        self.id = Book.__id_counter
