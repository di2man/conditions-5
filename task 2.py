def separate_numbers(numbers):
    even = []

    odd = []

    negative = []

    positive = []

    for num in numbers:

        if num % 2 == 0:

            even.append(num)

        else:

            odd.append(num)

        if num < 0:

            negative.append(num)

        else:

            positive.append(num)

    return even, odd, negative, positive


# Example usage

numbers = [3, -2, 7, 8, -5, 12, 1, 0, -9]

even, odd, negative, positive = separate_numbers(numbers)

print("Even numbers:", even)

print("Odd numbers:", odd)

print("Negative numbers:", negative)

print("Positive numbers:", positive)

