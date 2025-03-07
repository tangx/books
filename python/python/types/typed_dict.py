import json
from dataclasses import dataclass
from typing import Dict, Optional, Union


@dataclass
class Address:
    street: str
    city: str
    zip_code: str


@dataclass
class User:
    name: str
    age: int
    city: str
    address: Union[Address, None] = None
    addr: Optional[Address] = None


# You can use Optional[X] as a shorthand for Union[X, None].


user = User(name="John", age=30, city="New York")

usres: Dict[str, User] = {
    "user1": User(name="John", age=30, city="New York"),
    "user2": User(
        name="Tom",
        age=35,
        city="Chicago",
        address=Address("Main St", "Chicago", "12345"),
    ),
    "user3": User(
        name="Jane",
        age=25,
        city="Los Angeles",
        addr=Address("Main St", "Los Angeles", "12345"),
    ),
}

# print(usres)

user1 = usres["user1"]
# print(user1.addr.city)  # type: ignore

if user1.addr is not None:
    print(user.addr.city)
else:
    print("User has no address")

user2: User = usres["user2"]
print(user2.address.city)  # type: ignore


for k2, v2 in user2.__dict__.items():
    print(f"  {k2}: {v2}")


# 文件映射
with open("data.json", "w") as f:
    json.dump(usres, f, default=lambda o: o.__dict__)


with open("data.json", "r") as f:
    data = json.load(f)
    users2: Dict[str, User] = {k: User(**v) for k, v in data.items()}
    print(users2)
