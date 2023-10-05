


def oddnumber():
    random_numbers = [1,6,8,3,5,2,20,4,7]

    for number in random_numbers:

        if number % 2 == 0:
            continue

        print(number)


oddnumber()