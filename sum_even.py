def sum_even_numbers(numbers):
    sum_of_evens = 0
    for num in numbers:
        if num % 2 == 0:
            sum_of_evens += num
    return sum_of_evens

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(numbers_list)
print("Sum of even numbers:", result)
