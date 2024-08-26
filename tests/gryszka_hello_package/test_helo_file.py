from gryszka_hello_package.hello_file import hello, imported_another_hello

def test_hello():
    expected_return = "hello world returned"
    returned_message = hello()

    assert returned_message == expected_return

def test_imported_another_hello():
    expected_return = "another hello World returned"
    returned_message = imported_another_hello()

    assert returned_message == expected_return