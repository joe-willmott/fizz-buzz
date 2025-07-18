from main import fizz_buzz

def test_fizz_buzz():
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(5) == "Buzz"

    assert fizz_buzz(12) == "Fizz"
    assert fizz_buzz(20) == "Buzz"

    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(30) == "FizzBuzz"

    assert fizz_buzz(13) == "Nothing"