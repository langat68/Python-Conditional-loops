

for number in range (1,101):  # the range of the numbers
    if number % 3 == 0 and number % 5 == 0 : # modulus zero
        print("FizzBuz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)