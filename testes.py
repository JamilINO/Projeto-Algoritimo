import pytest

""" CODE """
def say_hello():
    name = input("What is your first name?")
    name2 = input("What is your last name?")
    print("Hello " + name + " " + name2)
    return "Hello " + name + " " + name2


if __name__ == "__main__":
    say_hello()

""" TEST """
class TestMy:
    def test_say_hello(monkeypatch):
        inputs = iter(['Pavol', 'Kutaj'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        result = say_hello()
        assert result == "Hello Pavol Kutaj"