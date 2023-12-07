def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
result = sum_even_numbers(number_list)
print(f"Sum of even numbers: {result}")
