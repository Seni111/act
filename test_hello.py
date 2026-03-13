from hello import greet, add

def test_greet():
    assert greet("Test") == "Hello, Test!"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0