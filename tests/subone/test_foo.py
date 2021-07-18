
from playground.subone.foo import Foo


def test_foo():
    assert Foo.double_something(2) == 4
