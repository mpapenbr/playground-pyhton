from playground.subone.foo import Foo
from playground.subtwo.sample import Sample


class Bar:
    def __init__(self) -> None:
        pass
    def do_something(self):
        print(f"i am Bar.do_something")
        pass

    def let_foo_do_something(self):
        print(f"i am in Bar an let Foo do_something")
        foo = Foo()
        foo.do_something()

    def let_sample_do_something(self):
        s = Sample()
        s.foo()
