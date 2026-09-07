from packaging import BaseModel


class User(BaseModel):
    name: str


def test_dummy():
    assert User(name="Ada").name == "Ada"
