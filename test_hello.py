from hello import greet, add


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_name():
    assert greet("Alice") == "Hello, Alice!"


def test_add():
    assert add(2, 3) == 5
