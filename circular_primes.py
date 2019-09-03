# Unsolved

def is_prime(num):
    for i in range(2, num):
       if num % i == 0:
           return False
    return True

def is_circular_prime(num):
    digits = str(num)

    for i in range(len(digits)):
        if not is_prime(int(digits[i:] + digits[:i])):
            return False

    return True

count = 0

for i in range(2, 1000000):
    if is_circular_prime(i):
        count += 1

print(count)
