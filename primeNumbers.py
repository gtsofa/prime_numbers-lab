def primeNumbers(number):
    number_list = []
    if type(number) != int:
        raise TypeError
    elif number <= 0:
        return number_list
    else:
        for i in range(2, number + 1):
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                number_list.append(i)

        return number_list
print(primeNumbers(10))
