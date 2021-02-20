# pytest + pytest-html

Test repository for [StackOverflow question PyTest: Interactive Output (instead
of pure
ASCII)](https://stackoverflow.com/questions/66225251/pytest-interactive-output-instead-of-pure-ascii).

```
$ pip install -r requirements.txt
$ pytest --showlocals --html=report.html --self-contained-html testmodule/test.py
=================================== test session starts ====================================
platform linux -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /tmp/test
plugins: html-3.1.1, metadata-1.11.0
collected 2 items

testmodule/test.py F.                                                                [100%]

========================================= FAILURES =========================================
_________________________________________ test_add _________________________________________

    def test_add():
        foo = 10
        bar = 12
>       assert add(foo, bar) == 22
E       assert -2 == 22
E        +  where -2 = add(10, 12)

bar        = 12
foo        = 10

testmodule/test.py:12: AssertionError
-------------------- generated html file: file:///tmp/test/report.html ---------------------
================================= short test summary info ==================================
FAILED testmodule/test.py::test_add - assert -2 == 22
=============================== 1 failed, 1 passed in 0.02s ================================
```

This will generate a `report.html` for you.
