from mypackage.core import Core

module = Core()


def test_1() -> None:
    assert module.add(1, 2) == 3
