from gryszka_another_package.another_hello_file import another_hello, imported_hello

def test_another_hello():
    expected_return = "another hello World returned"
    returned_message = another_hello()

    assert returned_message == expected_return

def test_imported_hello():
    expected_return = "hello world returned"
    returned_message = imported_hello()

    assert returned_message == expected_return