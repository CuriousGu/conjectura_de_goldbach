from typing import List, Union, Tuple


def main() -> None:
    number = int(input('Insert your number --> '))
    if number < 4 or number % 2 != 0:
        raise ValueError('Valor Inválido')

    array_to_check_sum = building_prime_list(number)

    result = find_sum(array_to_check_sum, number)
    print(print_answer(result, number))


# return True if the inserted parameter is a prime number
def check_prime(value: int) -> bool:
    answer = True

    if value == 1 or value == 0:
        raise ValueError('Indefinição Matemática!!')

    elif value > 1:
        for i in range(value):
            if i > 1:
                if value % i == 0:
                    answer = False

    return answer
    # true if prime
    # false if not prime


def building_prime_list(num: int) -> List[int]:
    prime_list = []

    if num < 4 and num % 2 != 0:
        raise ValueError('Número Inválido')

    for numbers in range(num):
        if numbers > 1:
            if check_prime(numbers):
                prime_list.append(numbers)

    return prime_list
    # return a list with all prime numbers less than the inserted value


def find_sum(prime_list: List[int], number: int) -> Union[bool, Tuple[int, int]]:
    index = 0

    while index < len(prime_list):
        for i in prime_list:
            if i + prime_list[index] == number:
                return i, prime_list[index]

        index += 1

    return False


def print_answer(result: Tuple[int, int], num: int) -> str:
    list(result).sort()
    return f'{result[0]} + {result[1]} = {num}'


if __name__ == '__main__':
    main()
