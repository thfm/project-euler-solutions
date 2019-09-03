# Unsolved

def is_prime(num):
    for i in range(2, num):
       if num % i == 0:
           return False
    return True

cardinal_counter = 1
prime_counter = 0

while prime_counter < 10001:
    cardinal_counter += 1
    if is_prime(cardinal_counter):
        prime_counter += 1

print(cardinal_counter)
