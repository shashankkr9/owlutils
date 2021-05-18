from owlutils import parsing


def test_safeint():
    assert parsing.safeint("123") == 123
    assert parsing.safeint("123-4") == None


def test_safeintorzero():
    assert parsing.safeintorzero("123") == 123
    assert parsing.safeintorzero("123-4") == 0


def test_safeintorbignumber():
    assert parsing.safeintorbignumber("123") == 123
    assert parsing.safeintorbignumber("123-4") == 10000000


def test_safefloat():
    assert parsing.safefloat("123.4") == 123.4
    assert parsing.safefloat("123-4") == None
