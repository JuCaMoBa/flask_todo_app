from dataclasses import dataclass

@dataclass
class UserDTO:
    id: int| None
    email: str
    name: str
    password: str

    



