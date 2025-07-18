def fizz_buzz(user_input):
    if user_input % 3 == 0 and user_input % 5 == 0:
        return "FizzBuzz"
    elif user_input % 3 == 0:
        return "Fizz"
    elif user_input % 5 == 0:
        return "Buzz"
    else:
        return "Nothing"