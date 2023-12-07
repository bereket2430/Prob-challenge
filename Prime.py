def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

input_num = 17
result = is_prime(input_num)
print(f"Is {input_num} a prime number? {result}")