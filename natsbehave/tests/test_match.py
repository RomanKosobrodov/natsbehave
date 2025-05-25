from natsbehave.compare import partially_equal


def test_partially_equal():
    d1 = {"one": 1, "two": 2, "three": 3}
    d2 = {"one": 1, "two": 2}

    assert partially_equal(d1, d2)
    assert partially_equal(d2, d1)

    assert not partially_equal(d1, {"one": 5})
    assert not partially_equal({"one": 5}, d1)

    assert not partially_equal({"value": 5}, d1)


def test_equal():
    d1 = {"one": 1, "two": 2, "three": 3}
    d2 = {"two": 2, "one": 1, "three": 3}
    assert d1 == d2


if __name__ == "__main__":
    test_partially_equal()
    test_equal()