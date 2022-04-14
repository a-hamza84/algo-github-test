from python_test import refined_main

def test_parse_commands():
    parse_commands= refined_main()[0]
    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
def test_copy_commands():
    copy_commands= refined_main()[1]
    assert copy_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
def test_functional_commands():
    functional_commands=refined_main()[2]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
def test_random_commands():
    random_commands=refined_main()[3]
    assert len(random_commands) == 2
def test_bad_commands():
    bad_commands=refined_main()[4]
    assert len(bad_commands) == 3