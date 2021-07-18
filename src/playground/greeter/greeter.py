class Greeter:
    def __init__(self) -> None:
        pass

    def greetings(self, name=None):
        if name == None:
            return f"Hello stranger"
        else:
            return f"Hello {name}"

